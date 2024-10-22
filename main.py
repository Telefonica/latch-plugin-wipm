import os
import sys
import json
import shutil
import posixpath
from typing import Literal
from string import Template

import dotenv
import latch
import mysql.connector
import paramiko
import requests
from mysql.connector import errorcode
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Slot

from about_gui import Ui_About
from installer_gui import Ui_MainWindow

WIPM_AGENT_PATH = "wipm-agent"
WIPM_AGENT_INSTALL_PATH = posixpath.join("/usr/local", WIPM_AGENT_PATH)

COMMAND_PIP = f"pip3 install -r {WIPM_AGENT_INSTALL_PATH}/requirements.txt"
COMMAND_GUNICORN = (
    f"gunicorn -b 0.0.0.0 -w 4 -k uvicorn.workers.UvicornWorker --chdir {WIPM_AGENT_INSTALL_PATH} -D main:app"
)

CONFIG_AGENT_FILE = "agent_config.json"
CONFIG_AGENT_PATH = os.path.join(os.path.expanduser("~"), f".{WIPM_AGENT_PATH}")
CONFIG_AGENT_FILE_PATH = os.path.join(CONFIG_AGENT_PATH, CONFIG_AGENT_FILE)

TRIGGERS_PATH = "queries/triggers"
TRIGGERS = [
    {"name": "before_wp_comments_insert", "action": "INSERT", "template": "readonly.sql"},
    {"name": "before_wp_comments_update", "action": "UPDATE", "template": "readonly.sql"},
    {"name": "before_wp_comments_delete", "action": "DELETE", "template": "readonly.sql"},
    {"name": "before_wp_posts_insert", "action": "INSERT", "template": "edition.sql"},
    {"name": "before_wp_posts_update", "action": "UPDATE", "template": "edition.sql"},
    {"name": "before_wp_posts_delete", "action": "DELETE", "template": "edition.sql"},
    {"name": "before_wp_users_insert", "action": "INSERT", "template": "admin_user.sql"},
    {"name": "before_wp_users_update", "action": "UPDATE", "template": "admin_user.sql"},
    {"name": "before_wp_users_delete", "action": "DELETE", "template": "admin_user.sql"},
    {"name": "before_wp_usermeta_insert", "action": "INSERT", "variable": "NEW", "template": "admin.sql"},
    {"name": "before_wp_usermeta_update", "action": "UPDATE", "variable": "NEW", "template": "admin.sql"},
    {"name": "before_wp_usermeta_delete", "action": "DELETE", "variable": "OLD", "template": "admin.sql"},
]

cnx = None
db_accounts = []

wipm_config = None
latch_config = None

triggers_enabled = False
logs_enabled = False


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class About(QWidget):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)


class WiPMConfig:
    def __init__(self, db, host, port, password):
        self.db = db
        self.db_user = None
        self.host = host
        self.port = port
        self.password = password

    def set_db_user(self, db_user):
        self.db_user = db_user


class LatchConfig:
    def __init__(self, app_id, secret, account_id):
        self.app_id = app_id
        self.secret = secret
        self.account_id = account_id
        self.read_only_op = None
        self.edition_op = None
        self.admin_op = None

    def set_read_only_op(self, read_only_op):
        self.read_only_op = read_only_op

    def set_edition_op(self, edition_op):
        self.edition_op = edition_op

    def set_admin_op(self, admin_op):
        self.admin_op = admin_op


def read_config():
    with open(CONFIG_AGENT_FILE_PATH, "r") as f:
        return json.load(f)


def save_config(host, port=8000):
    agent_config = {
        "host": host,
        "port": port,
    }

    try:
        os.mkdir(CONFIG_AGENT_PATH)
    except FileExistsError:
        pass

    with open(CONFIG_AGENT_FILE_PATH, "w") as f:
        f.write(json.dumps(agent_config))


def connect_db(config):
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        window.ui.test_db_connection_msg.setStyleSheet("color: red;")
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            window.ui.test_db_connection_msg.setText("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            window.ui.test_db_connection_msg.setText("Database does not exist")
        else:
            window.ui.test_db_connection_msg.setText(str(err))
    return None


def execute_query(query: str, params: tuple = None):
    global cnx
    if cnx and cnx.is_connected():
        print("Executing query...")
        with cnx.cursor() as cursor:
            cursor.execute(query, params)
            cnx.commit()


def add_latch_row(latch_id: str, latch_name: str, latch_status: Literal["on", "off"]):
    query = "INSERT INTO latch.latch (operation_id, operation_name, latch) VALUES (%s, %s, %s);"
    execute_query(query, (latch_id, latch_name, latch_status))


def create_operations(latch_api, latch_config):
    latch_operations = ["ReadOnly", "Edition", "Administration"]

    operations = latch_api.get_operations().data
    for operation_id, operation_data in operations["operations"].items():
        if operation_data["name"] in latch_operations:
            operation_name = operation_data["name"]
            operation_status = latch_api.operation_status(latch_config.account_id, operation_id).data["operations"][
                operation_id
            ]["status"]

            add_latch_row(operation_id, operation_name, operation_status)
            if operation_name == "ReadOnly":
                latch_config.set_read_only_op(operation_id)
            elif operation_name == "Edition":
                latch_config.set_edition_op(operation_id)
            elif operation_name == "Administration":
                latch_config.set_admin_op(operation_id)
            latch_operations.remove(operation_name)

    for latch in latch_operations:
        operation = latch_api.create_operation(latch_config.app_id, latch, "DISABLED", "DISABLED").get_data()
        add_latch_row(operation["operationId"], latch, "on")
        if latch == "ReadOnly":
            latch_config.set_read_only_op(operation["operationId"])
        elif latch == "Edition":
            latch_config.set_edition_op(operation["operationId"])
        elif latch == "Administration":
            latch_config.set_admin_op(operation["operationId"])


def clear_messages():
    window.ui.main_msg.setText("")
    window.ui.test_db_connection_msg.setText("")
    window.ui.pair_with_latch_msg.setText("")
    window.ui.opt_msg.setText("")
    window.ui.ssh_upload_msg.setText("")
    window.ui.local_copy_msg.setText("")


def print_msg(widget, msg, msg_type):
    color = {"info": "green", "warning": "orange", "error": "red"}.get(msg_type, "black")
    widget.setStyleSheet(f"color: {color};")
    widget.setText(msg)


def get_actual_page():
    return window.ui.stackedWidget.currentIndex()


def next_page():
    global wipm_config

    clear_messages()
    window.ui.stackedWidget.setCurrentIndex(get_actual_page() + 1)
    window.ui.go_back_button.setVisible(True)

    if get_actual_page() == 1:
        window.ui.next_button.setDisabled(True)

    if get_actual_page() == 2:
        window.ui.wp_select_user_combo.clear()
        window.ui.wp_select_user_combo.addItems(db_accounts)
        window.ui.next_button.setDisabled(False)

    if get_actual_page() == 3:
        wp_user = window.ui.wp_select_user_combo.currentText()
        init_db(wp_user)
        wipm_config.set_db_user(wp_user)
        window.ui.next_button.setDisabled(True)

    if get_actual_page() == 4:
        window.ui.next_button.setDisabled(True)

    if get_actual_page() == 5:
        window.ui.local_remote.setCurrentIndex(0)
        window.ui.local_radio_btn.setChecked(True)
        window.ui.next_button.setVisible(False)

        if not sys.platform.startswith("linux"):
            window.ui.local_copy_btn.setDisabled(True)
            print_msg(window.ui.local_copy_msg, "⚠ Local copy only available for Linux", "warning")


def go_back():
    clear_messages()
    window.ui.stackedWidget.setCurrentIndex(get_actual_page() - 1)
    window.ui.next_button.setDisabled(False)

    if get_actual_page() == 0:
        window.ui.go_back_button.setVisible(False)
        window.ui.next_button.setVisible(False)

    if get_actual_page() == 1:
        window.ui.go_back_button.setVisible(False)
        window.ui.next_button.setDisabled(True)
        window.ui.test_db_connection_msg.setText("")

    if get_actual_page() == 4:
        window.ui.next_button.setVisible(True)


def init_db(wordpress_user):
    with open("queries/init.sql", "r") as f:
        query = Template(f.read())
        result = query.substitute(wordpress_user=wordpress_user)

        for q in result.split(";"):
            execute_query(q.strip())


def check_triggers():
    # Read triggers
    global cnx
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            try:
                cursor.execute(f"USE {wipm_config.db}")
                cursor.execute("SHOW TRIGGERS")
                cursor.fetchall()
                if cursor.rowcount >= 11:
                    print("Triggers already created")
                    return True
                print("No all triggers found")
                return False
            except Exception as e:
                print("Exception: No triggers found")


def create_env_file():
    env_file = os.path.join(WIPM_AGENT_PATH, ".env")
    try:
        dotenv.set_key(env_file, "DB_HOST", wipm_config.host)
        dotenv.set_key(env_file, "DB_PORT", wipm_config.port)
        dotenv.set_key(env_file, "DB_USER", wipm_config.db_user)
        dotenv.set_key(env_file, "DB_PASSWORD", wipm_config.password)
        dotenv.set_key(env_file, "DB_NAME", wipm_config.db)
        dotenv.set_key(env_file, "LATCH_APP_ID", latch_config.app_id)
        dotenv.set_key(env_file, "LATCH_SECRET_KEY", latch_config.secret)
        dotenv.set_key(env_file, "LATCH_ACCOUNT_ID", latch_config.account_id)
        dotenv.set_key(env_file, "LATCH_READ_ONLY_OP", latch_config.read_only_op)
        dotenv.set_key(env_file, "LATCH_EDITION_OP", latch_config.edition_op)
        dotenv.set_key(env_file, "LATCH_ADMIN_OP", latch_config.admin_op)
    except Exception as e:
        print(f"Error creating .env file: {e}")


@Slot()
def install_wipm():
    window.ui.stackedWidget.setCurrentIndex(1)
    window.ui.go_back_button.setVisible(True)
    window.ui.next_button.setDisabled(True)
    window.ui.next_button.setVisible(True)


@Slot()
def check_service_status():
    host_config = read_config()
    try:
        response = requests.get(f"http://{host_config['host']}:{host_config['port']}/ping")
        if response.status_code == 200:
            print_msg(window.ui.main_msg, "Service is running!", "info")
        else:
            print_msg(window.ui.main_msg, "Service is not running!", "error")
    except requests.exceptions.ConnectionError:
        print_msg(window.ui.main_msg, "Service is not running!", "error")


@Slot()
def test_db_connection():
    global cnx
    global db_accounts
    global wipm_config

    config = {}
    config["user"] = (
        window.ui.db_username_input.text()
        if window.ui.db_username_input.text() != ""
        else window.ui.db_username_input.placeholderText()
    )
    config["password"] = window.ui.db_password_input.text()
    config["host"] = (
        window.ui.db_host_input.text()
        if window.ui.db_host_input.text() != ""
        else window.ui.db_host_input.placeholderText()
    )
    config["port"] = (
        window.ui.db_port_input.text()
        if window.ui.db_port_input.text() != ""
        else window.ui.db_port_input.placeholderText()
    )
    config["database"] = (
        window.ui.db_database_input.text()
        if window.ui.db_database_input.text() != ""
        else window.ui.db_database_input.placeholderText()
    )

    wipm_config = WiPMConfig(
        db=config["database"],
        host=config["host"],
        port=config["port"],
        password=config["password"],
    )

    cnx = connect_db(config)
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT user,host FROM mysql.user WHERE host!='localhost' AND user!='root' AND user!='latch'"
                )
                rows = cursor.fetchall()
                for row in rows:
                    db_accounts.append(row[0])

                # Enable the next button
                window.ui.next_button.setDisabled(False)
                print_msg(window.ui.test_db_connection_msg, "Connection successful!", "info")
            except mysql.connector.Error as err:
                print_msg(
                    window.ui.test_db_connection_msg,
                    f"{str(err)}\nAre you sure the user has the right permissions?",
                    "error",
                )


@Slot()
def pair_with_latch():
    global latch_config

    if latch_config:
        print_msg(window.ui.pair_with_latch_msg, "You have already paired with Latch", "error")
        return

    # Get the values from the input fields
    latch_app_id = window.ui.latch_app_id_input.text()
    latch_secret = window.ui.latch_secret_input.text()
    latch_pair_code = window.ui.latch_pair_code_input.text()

    if latch_app_id == "" or latch_secret == "" or latch_pair_code == "":
        print_msg(window.ui.pair_with_latch_msg, "Please fill all the fields", "error")
        return

    api = latch.Latch(latch_app_id, latch_secret)
    response = api.pair(latch_pair_code)
    responseData = response.get_data()
    responseError = response.get_error()

    if responseError:
        print_msg(window.ui.pair_with_latch_msg, responseError.message, "error")
        return

    latch_config = LatchConfig(latch_app_id, latch_secret, responseData["accountId"])

    create_operations(api, latch_config)
    create_env_file()

    print_msg(window.ui.pair_with_latch_msg, "Pairing successful!", "info")
    window.ui.pair_with_latch_btn.setDisabled(True)
    window.ui.next_button.setDisabled(False)


@Slot()
def create_triggers():
    global cnx
    global triggers_enabled
    global wipm_config

    if check_triggers():
        print_msg(window.ui.opt_msg, "Triggers already created", "info")

        triggers_enabled = True

        if triggers_enabled and logs_enabled:
            window.ui.next_button.setDisabled(False)
        return

    print("Creating triggers...")
    execute_query("SET GLOBAL log_bin_trust_function_creators = 1")

    for trigger in TRIGGERS:
        with open(os.path.join(TRIGGERS_PATH, trigger["template"]), "r") as f:
            query = Template(f.read())
            mapping = {
                "trigger_name": trigger["name"],
                "action": trigger["action"],
                "wordpress_db": wipm_config.db,
                "wordpress_user": wipm_config.db_user,
            }

            if trigger.get("variable"):
                mapping["variable"] = trigger["variable"]

            result = query.substitute(mapping)

            try:
                with cnx.cursor() as cursor:
                    cursor.execute(result)
            except Exception as e:
                print(f"Error executing trigger: {trigger['action']}, {trigger['name']}")
                print_msg(window.ui.opt_msg, f"Error executing trigger: {e}", "error")
                return

    execute_query("SET GLOBAL log_bin_trust_function_creators = 0;")

    print_msg(window.ui.opt_msg, "Triggers created successfully!", "info")
    triggers_enabled = True
    if triggers_enabled and logs_enabled:
        window.ui.next_button.setDisabled(False)


@Slot()
def enable_db_logs():
    execute_query("SET GLOBAL general_log=0")
    execute_query("TRUNCATE table mysql.general_log")
    execute_query("SET GLOBAL general_log=1")
    execute_query("SET GLOBAL log_output='TABLE'")
    print_msg(window.ui.opt_msg, "Logs enabled successfully!", "info")

    global logs_enabled
    logs_enabled = True

    if triggers_enabled and logs_enabled:
        window.ui.next_button.setDisabled(False)


@Slot()
def view_local_agent():
    window.ui.local_remote.setCurrentIndex(0)


@Slot()
def view_remote_agent():
    window.ui.local_remote.setCurrentIndex(1)


@Slot()
def copy_wipm_agent():
    print_msg(window.ui.local_copy_msg, "Installing agent...", "warning")
    try:
        shutil.copytree(WIPM_AGENT_PATH, WIPM_AGENT_INSTALL_PATH)
    except Exception:
        print_msg(window.ui.local_copy_msg, "Agent already copied", "warning")
    finally:
        # Install requirements
        os.system(COMMAND_PIP)
        save_config("127.0.0.1")
    os.system(COMMAND_GUNICORN)
    print_msg(window.ui.local_copy_msg, "WiPM Agent running!", "info")


@Slot()
def upload_wipm_agent():
    host = window.ui.ssh_host_input.text()
    username = window.ui.ssh_user_input.text()
    password = window.ui.ssh_pass_input.text()

    try:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)

        sftp = client.open_sftp()
        try:
            sftp.chdir("/usr/local")
            sftp.mkdir(WIPM_AGENT_PATH)
        except FileNotFoundError:
            print_msg(window.ui.ssh_upload_msg, "/usr/local path doesn't exist, is it a Linux machine?", "error")
            sftp.close()
            client.close()
            return
        except PermissionError:
            print_msg(window.ui.ssh_upload_msg, "Permission denied, are you root?", "error")
            sftp.close()
            client.close()
            return
        except OSError as e:
            print("Directory already exists, continuing...")
        except Exception as e:
            print(f"Error: {e}")
            sftp.close()
            client.close()
            return

        for item in os.listdir(WIPM_AGENT_PATH):
            localpath = os.path.join(WIPM_AGENT_PATH, item)
            sftp.put(localpath, f"/usr/local/{WIPM_AGENT_PATH}/{item}")

        sftp.close()

        save_config(host)

        # Install requirements
        client.exec_command(COMMAND_PIP)
        client.exec_command(COMMAND_GUNICORN)
        client.close()
        print_msg(window.ui.ssh_upload_msg, "WiPM Agent uploaded and running!", "info")

    except Exception as e:
        print_msg(window.ui.ssh_upload_msg, "Error uploading the agent", "error")
        try:
            client.close()
        except:
            pass
        finally:
            return


@Slot()
def show_about():
    about.show()


if __name__ == "__main__":
    if sys.platform.startswith("linux"):
        if os.geteuid() != 0:
            print("Please run this script as root")
            sys.exit(1)

    app = QApplication(sys.argv)

    window = MainWindow()

    if os.path.exists(CONFIG_AGENT_FILE_PATH):
        window.ui.stackedWidget.setCurrentIndex(0)
        window.ui.next_button.setVisible(False)
    else:
        window.ui.stackedWidget.setCurrentIndex(1)

    window.show()

    # Connect the buttons to the slots
    window.ui.install_wipm_btn.clicked.connect(install_wipm)
    window.ui.check_srv_btn.clicked.connect(check_service_status)
    window.ui.test_db_connection_btn.clicked.connect(test_db_connection)
    window.ui.pair_with_latch_btn.clicked.connect(pair_with_latch)
    window.ui.opt_triggers_btn.clicked.connect(create_triggers)
    window.ui.opt_logs_btn.clicked.connect(enable_db_logs)
    window.ui.local_copy_btn.clicked.connect(copy_wipm_agent)
    window.ui.ssh_upload_btn.clicked.connect(upload_wipm_agent)

    # Connect radio buttons
    window.ui.local_radio_btn.toggled.connect(view_local_agent)
    window.ui.remote_radio_btn.toggled.connect(view_remote_agent)

    # On start, clear the messages
    clear_messages()

    # On start, disable go back button and next button
    window.ui.go_back_button.setVisible(False)
    window.ui.next_button.setDisabled(True)

    # Buttons to navigate between pages
    window.ui.next_button.clicked.connect(next_page)
    window.ui.go_back_button.clicked.connect(go_back)

    # About dialog
    about = About()
    window.ui.actionAbout.triggered.connect(show_about)

    sys.exit(app.exec())
