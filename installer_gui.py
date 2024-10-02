# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wipmnVjkOU.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
import wipm_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 400)
        MainWindow.setMinimumSize(QSize(655, 0))
        MainWindow.setMaximumSize(QSize(655, 400))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header_text = QLabel(self.centralwidget)
        self.header_text.setObjectName("header_text")
        font = QFont()
        font.setFamilies(["Telefonica Sans"])
        self.header_text.setFont(font)
        self.header_text.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_3.addWidget(self.header_text)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.installer_img = QLabel(self.centralwidget)
        self.installer_img.setObjectName("installer_img")
        self.installer_img.setMaximumSize(QSize(150, 300))
        self.installer_img.setFrameShape(QFrame.Shape.StyledPanel)
        self.installer_img.setFrameShadow(QFrame.Shadow.Sunken)
        self.installer_img.setPixmap(QPixmap(":/img/resources/installer.png"))
        self.installer_img.setScaledContents(True)
        self.installer_img.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.installer_img)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.install_wipm_btn = QPushButton(self.page)
        self.install_wipm_btn.setObjectName("install_wipm_btn")

        self.verticalLayout_4.addWidget(self.install_wipm_btn)

        self.check_srv_btn = QPushButton(self.page)
        self.check_srv_btn.setObjectName("check_srv_btn")

        self.verticalLayout_4.addWidget(self.check_srv_btn)

        self.main_msg = QLabel(self.page)
        self.main_msg.setObjectName("main_msg")
        self.main_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_msg.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.main_msg)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.db_desc = QLabel(self.page_1)
        self.db_desc.setObjectName("db_desc")
        self.db_desc.setFont(font)
        self.db_desc.setWordWrap(True)

        self.verticalLayout.addWidget(self.db_desc)

        self.db_config = QGridLayout()
        self.db_config.setObjectName("db_config")
        self.db_port = QLabel(self.page_1)
        self.db_port.setObjectName("db_port")
        self.db_port.setFont(font)

        self.db_config.addWidget(self.db_port, 0, 2, 1, 1)

        self.db_database = QLabel(self.page_1)
        self.db_database.setObjectName("db_database")
        self.db_database.setFont(font)

        self.db_config.addWidget(self.db_database, 3, 0, 1, 1)

        self.db_host = QLabel(self.page_1)
        self.db_host.setObjectName("db_host")
        self.db_host.setFont(font)

        self.db_config.addWidget(self.db_host, 0, 0, 1, 1)

        self.db_password = QLabel(self.page_1)
        self.db_password.setObjectName("db_password")
        self.db_password.setFont(font)

        self.db_config.addWidget(self.db_password, 2, 0, 1, 1)

        self.db_host_input = QLineEdit(self.page_1)
        self.db_host_input.setObjectName("db_host_input")

        self.db_config.addWidget(self.db_host_input, 0, 1, 1, 1)

        self.db_username = QLabel(self.page_1)
        self.db_username.setObjectName("db_username")
        self.db_username.setFont(font)

        self.db_config.addWidget(self.db_username, 1, 0, 1, 1)

        self.db_port_input = QLineEdit(self.page_1)
        self.db_port_input.setObjectName("db_port_input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_port_input.sizePolicy().hasHeightForWidth())
        self.db_port_input.setSizePolicy(sizePolicy)

        self.db_config.addWidget(self.db_port_input, 0, 3, 1, 1)

        self.db_username_input = QLineEdit(self.page_1)
        self.db_username_input.setObjectName("db_username_input")

        self.db_config.addWidget(self.db_username_input, 1, 1, 1, 3)

        self.db_password_input = QLineEdit(self.page_1)
        self.db_password_input.setObjectName("db_password_input")
        self.db_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.db_config.addWidget(self.db_password_input, 2, 1, 1, 3)

        self.db_database_input = QLineEdit(self.page_1)
        self.db_database_input.setObjectName("db_database_input")

        self.db_config.addWidget(self.db_database_input, 3, 1, 1, 3)

        self.verticalLayout.addLayout(self.db_config)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.test_db_connection_btn = QPushButton(self.page_1)
        self.test_db_connection_btn.setObjectName("test_db_connection_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.test_db_connection_btn.sizePolicy().hasHeightForWidth())
        self.test_db_connection_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.test_db_connection_btn)

        self.test_db_connection_msg = QLabel(self.page_1)
        self.test_db_connection_msg.setObjectName("test_db_connection_msg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.test_db_connection_msg.sizePolicy().hasHeightForWidth())
        self.test_db_connection_msg.setSizePolicy(sizePolicy2)
        self.test_db_connection_msg.setFont(font)
        self.test_db_connection_msg.setWordWrap(True)

        self.horizontalLayout.addWidget(self.test_db_connection_msg)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.wp_config = QGridLayout()
        self.wp_config.setObjectName("wp_config")
        self.wp_select_user = QLabel(self.page_2)
        self.wp_select_user.setObjectName("wp_select_user")
        self.wp_select_user.setFont(font)

        self.wp_config.addWidget(self.wp_select_user, 0, 0, 1, 1)

        self.wp_select_user_combo = QComboBox(self.page_2)
        self.wp_select_user_combo.setObjectName("wp_select_user_combo")

        self.wp_config.addWidget(self.wp_select_user_combo, 0, 1, 1, 1)

        self.gridLayout_6.addLayout(self.wp_config, 1, 0, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pair_with_latch_btn = QPushButton(self.page_3)
        self.pair_with_latch_btn.setObjectName("pair_with_latch_btn")
        sizePolicy1.setHeightForWidth(self.pair_with_latch_btn.sizePolicy().hasHeightForWidth())
        self.pair_with_latch_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.pair_with_latch_btn)

        self.pair_with_latch_msg = QLabel(self.page_3)
        self.pair_with_latch_msg.setObjectName("pair_with_latch_msg")
        sizePolicy2.setHeightForWidth(self.pair_with_latch_msg.sizePolicy().hasHeightForWidth())
        self.pair_with_latch_msg.setSizePolicy(sizePolicy2)
        self.pair_with_latch_msg.setFont(font)
        self.pair_with_latch_msg.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.pair_with_latch_msg)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.latch_config = QGridLayout()
        self.latch_config.setObjectName("latch_config")
        self.latch_app_id = QLabel(self.page_3)
        self.latch_app_id.setObjectName("latch_app_id")
        self.latch_app_id.setFont(font)

        self.latch_config.addWidget(self.latch_app_id, 0, 0, 1, 1)

        self.latch_secret = QLabel(self.page_3)
        self.latch_secret.setObjectName("latch_secret")
        self.latch_secret.setFont(font)

        self.latch_config.addWidget(self.latch_secret, 1, 0, 1, 1)

        self.latch_app_id_input = QLineEdit(self.page_3)
        self.latch_app_id_input.setObjectName("latch_app_id_input")

        self.latch_config.addWidget(self.latch_app_id_input, 0, 1, 1, 1)

        self.latch_secret_input = QLineEdit(self.page_3)
        self.latch_secret_input.setObjectName("latch_secret_input")

        self.latch_config.addWidget(self.latch_secret_input, 1, 1, 1, 1)

        self.latch_pair_code = QLabel(self.page_3)
        self.latch_pair_code.setObjectName("latch_pair_code")
        self.latch_pair_code.setFont(font)

        self.latch_config.addWidget(self.latch_pair_code, 2, 0, 1, 1)

        self.latch_pair_code_input = QLineEdit(self.page_3)
        self.latch_pair_code_input.setObjectName("latch_pair_code_input")

        self.latch_config.addWidget(self.latch_pair_code_input, 2, 1, 1, 1)

        self.gridLayout_3.addLayout(self.latch_config, 1, 0, 1, 1)

        self.latch_desc = QLabel(self.page_3)
        self.latch_desc.setObjectName("latch_desc")
        self.latch_desc.setFont(font)
        self.latch_desc.setWordWrap(True)
        self.latch_desc.setOpenExternalLinks(True)

        self.gridLayout_3.addWidget(self.latch_desc, 0, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout = QGridLayout(self.page_4)
        self.gridLayout.setObjectName("gridLayout")
        self.opt_logs_btn = QPushButton(self.page_4)
        self.opt_logs_btn.setObjectName("opt_logs_btn")

        self.gridLayout.addWidget(self.opt_logs_btn, 2, 0, 1, 1)

        self.opt_desc = QLabel(self.page_4)
        self.opt_desc.setObjectName("opt_desc")
        self.opt_desc.setFont(font)
        self.opt_desc.setWordWrap(True)

        self.gridLayout.addWidget(self.opt_desc, 0, 0, 1, 1)

        self.opt_msg = QLabel(self.page_4)
        self.opt_msg.setObjectName("opt_msg")
        sizePolicy2.setHeightForWidth(self.opt_msg.sizePolicy().hasHeightForWidth())
        self.opt_msg.setSizePolicy(sizePolicy2)
        self.opt_msg.setFont(font)
        self.opt_msg.setWordWrap(True)

        self.gridLayout.addWidget(self.opt_msg, 3, 0, 1, 1)

        self.opt_triggers_btn = QPushButton(self.page_4)
        self.opt_triggers_btn.setObjectName("opt_triggers_btn")

        self.gridLayout.addWidget(self.opt_triggers_btn, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_4 = QGridLayout(self.page_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.local_radio_btn = QRadioButton(self.page_5)
        self.local_radio_btn.setObjectName("local_radio_btn")
        self.local_radio_btn.setChecked(True)

        self.gridLayout_4.addWidget(self.local_radio_btn, 1, 0, 1, 1)

        self.description_copy = QLabel(self.page_5)
        self.description_copy.setObjectName("description_copy")
        self.description_copy.setFont(font)
        self.description_copy.setWordWrap(True)

        self.gridLayout_4.addWidget(self.description_copy, 0, 0, 1, 1)

        self.remote_radio_btn = QRadioButton(self.page_5)
        self.remote_radio_btn.setObjectName("remote_radio_btn")

        self.gridLayout_4.addWidget(self.remote_radio_btn, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.page_5)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.local_remote = QStackedWidget(self.groupBox)
        self.local_remote.setObjectName("local_remote")
        self.page_local = QWidget()
        self.page_local.setObjectName("page_local")
        self.verticalLayout_5 = QVBoxLayout(self.page_local)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.local_copy_btn = QPushButton(self.page_local)
        self.local_copy_btn.setObjectName("local_copy_btn")

        self.verticalLayout_5.addWidget(self.local_copy_btn)

        self.local_copy_msg = QLabel(self.page_local)
        self.local_copy_msg.setObjectName("local_copy_msg")

        self.verticalLayout_5.addWidget(self.local_copy_msg)

        self.local_copy_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.local_copy_spacer)

        self.local_remote.addWidget(self.page_local)
        self.page_remote = QWidget()
        self.page_remote.setObjectName("page_remote")
        self.verticalLayout_6 = QVBoxLayout(self.page_remote)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ssh_user = QLabel(self.page_remote)
        self.ssh_user.setObjectName("ssh_user")
        self.ssh_user.setFont(font)

        self.gridLayout_5.addWidget(self.ssh_user, 1, 0, 1, 1)

        self.ssh_port = QLabel(self.page_remote)
        self.ssh_port.setObjectName("ssh_port")
        self.ssh_port.setFont(font)

        self.gridLayout_5.addWidget(self.ssh_port, 0, 2, 1, 1)

        self.ssh_host_input = QLineEdit(self.page_remote)
        self.ssh_host_input.setObjectName("ssh_host_input")

        self.gridLayout_5.addWidget(self.ssh_host_input, 0, 1, 1, 1)

        self.ssh_pass = QLabel(self.page_remote)
        self.ssh_pass.setObjectName("ssh_pass")
        self.ssh_pass.setFont(font)

        self.gridLayout_5.addWidget(self.ssh_pass, 2, 0, 1, 1)

        self.ssh_user_input = QLineEdit(self.page_remote)
        self.ssh_user_input.setObjectName("ssh_user_input")

        self.gridLayout_5.addWidget(self.ssh_user_input, 1, 1, 1, 3)

        self.ssh_pass_input = QLineEdit(self.page_remote)
        self.ssh_pass_input.setObjectName("ssh_pass_input")
        self.ssh_pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_5.addWidget(self.ssh_pass_input, 2, 1, 1, 3)

        self.ssh_host = QLabel(self.page_remote)
        self.ssh_host.setObjectName("ssh_host")
        self.ssh_host.setFont(font)

        self.gridLayout_5.addWidget(self.ssh_host, 0, 0, 1, 1)

        self.ssh_port_input = QLineEdit(self.page_remote)
        self.ssh_port_input.setObjectName("ssh_port_input")
        sizePolicy.setHeightForWidth(self.ssh_port_input.sizePolicy().hasHeightForWidth())
        self.ssh_port_input.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.ssh_port_input, 0, 3, 1, 1)

        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ssh_upload_btn = QPushButton(self.page_remote)
        self.ssh_upload_btn.setObjectName("ssh_upload_btn")
        sizePolicy1.setHeightForWidth(self.ssh_upload_btn.sizePolicy().hasHeightForWidth())
        self.ssh_upload_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.ssh_upload_btn)

        self.ssh_upload_msg = QLabel(self.page_remote)
        self.ssh_upload_msg.setObjectName("ssh_upload_msg")
        sizePolicy2.setHeightForWidth(self.ssh_upload_msg.sizePolicy().hasHeightForWidth())
        self.ssh_upload_msg.setSizePolicy(sizePolicy2)
        self.ssh_upload_msg.setFont(font)
        self.ssh_upload_msg.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.ssh_upload_msg)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.local_remote.addWidget(self.page_remote)

        self.verticalLayout_7.addWidget(self.local_remote)

        self.gridLayout_4.addWidget(self.groupBox, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.wizard_btn = QHBoxLayout()
        self.wizard_btn.setObjectName("wizard_btn")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.wizard_btn.addItem(self.horizontalSpacer)

        self.go_back_button = QPushButton(self.centralwidget)
        self.go_back_button.setObjectName("go_back_button")

        self.wizard_btn.addWidget(self.go_back_button)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName("next_button")

        self.wizard_btn.addWidget(self.next_button)

        self.verticalLayout_2.addLayout(self.wizard_btn)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.footer = QHBoxLayout()
        self.footer.setObjectName("footer")
        self.footer.setContentsMargins(-1, 0, -1, -1)
        self.footer_text = QWidget(self.centralwidget)
        self.footer_text.setObjectName("footer_text")
        sizePolicy1.setHeightForWidth(self.footer_text.sizePolicy().hasHeightForWidth())
        self.footer_text.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_text)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.powered_msg = QLabel(self.footer_text)
        self.powered_msg.setObjectName("powered_msg")
        self.powered_msg.setFont(font)

        self.horizontalLayout_5.addWidget(self.powered_msg)

        self.logo_footer = QLabel(self.footer_text)
        self.logo_footer.setObjectName("logo_footer")
        self.logo_footer.setMaximumSize(QSize(69, 25))
        self.logo_footer.setPixmap(QPixmap(":/img/resources/logo_latch.svg"))
        self.logo_footer.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.logo_footer)

        self.footer.addWidget(self.footer_text)

        self.verticalLayout_3.addLayout(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 655, 24))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        # if QT_CONFIG(shortcut)
        self.db_port.setBuddy(self.db_port_input)
        self.db_database.setBuddy(self.db_database_input)
        self.db_host.setBuddy(self.db_host_input)
        self.db_password.setBuddy(self.db_password_input)
        self.db_username.setBuddy(self.db_username_input)
        self.wp_select_user.setBuddy(self.wp_select_user_combo)
        self.latch_app_id.setBuddy(self.latch_app_id_input)
        self.latch_secret.setBuddy(self.latch_secret_input)
        self.latch_pair_code.setBuddy(self.latch_pair_code_input)
        self.ssh_user.setBuddy(self.ssh_user_input)
        self.ssh_port.setBuddy(self.ssh_port_input)
        self.ssh_pass.setBuddy(self.ssh_pass_input)
        self.ssh_host.setBuddy(self.ssh_host_input)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.next_button, self.go_back_button)

        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.local_remote.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "WiPM Installer", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "Information", None))
        self.header_text.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:24pt; font-weight:700;">WordPress in Paranoid Mode</span></p></body></html>',
                None,
            )
        )
        self.installer_img.setText("")
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>A WiPM agent <span style=" font-weight:700;">configuration has been detected</span>, do you want to check the status of the service or do you want to perform a new installation?</p></body></html>',
                None,
            )
        )
        self.install_wipm_btn.setText(
            QCoreApplication.translate("MainWindow", "Install WordPress in Paranoid Mode", None)
        )
        self.check_srv_btn.setText(QCoreApplication.translate("MainWindow", "Check WiPM status", None))
        self.main_msg.setText(QCoreApplication.translate("MainWindow", "main_msg", None))
        self.db_desc.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Inserts the <span style=" font-weight:700;">connection to the database</span>. The user must have root privileges, since a new user and a new database will be created for control through Latch.</p></body></html>',
                None,
            )
        )
        self.db_port.setText(QCoreApplication.translate("MainWindow", "Port", None))
        self.db_database.setText(QCoreApplication.translate("MainWindow", "Database", None))
        self.db_host.setText(QCoreApplication.translate("MainWindow", "Server Host", None))
        self.db_password.setText(QCoreApplication.translate("MainWindow", "Password", None))
        self.db_host_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "localhost", None))
        self.db_username.setText(QCoreApplication.translate("MainWindow", "Username", None))
        self.db_port_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "3306", None))
        self.db_username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "root", None))
        self.db_database_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "wordpress", None))
        self.test_db_connection_btn.setText(QCoreApplication.translate("MainWindow", "Connect", None))
        self.test_db_connection_msg.setText(QCoreApplication.translate("MainWindow", "test_db_connection_msg", None))
        self.wp_select_user.setText(QCoreApplication.translate("MainWindow", "Wordpress database user", None))
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:700;">Select the database user used to configure WordPress.</span></p><p>Triggers will be created to control the actions of this user on the WordPress database.</p></body></html>',
                None,
            )
        )
        self.pair_with_latch_btn.setText(QCoreApplication.translate("MainWindow", "Pair with Latch", None))
        self.pair_with_latch_msg.setText(QCoreApplication.translate("MainWindow", "pair_with_latch_msg", None))
        self.latch_app_id.setText(QCoreApplication.translate("MainWindow", "App ID", None))
        self.latch_secret.setText(QCoreApplication.translate("MainWindow", "Secret", None))
        self.latch_pair_code.setText(QCoreApplication.translate("MainWindow", "Pair code", None))
        self.latch_desc.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Enter the <a href="https://latch.tu.com/www/secure/login"><span style=" text-decoration: underline; color:#094fd1;">Latch application data</span></a> and the user code to protect the WordPress database and create a latch with operations. You can obtain your user code in the Latch mobile application by selecting \'<span style=" font-weight:700; font-style:italic;">Add latch</span>\'.</p></body></html>',
                None,
            )
        )
        self.opt_logs_btn.setText(QCoreApplication.translate("MainWindow", "Enable Logs", None))
        self.opt_desc.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>It is necessary, firstly, to <span style=" font-weight:700;">create triggers</span> to ensure that the latch status is automatically checked before allowing certain actions in the database, such as deleting records.</p><p>Secondly, it is also necessary, to <span style=" font-weight:700;">enable logs</span> so that database actions are recorded and stored in a table.</p></body></html>',
                None,
            )
        )
        self.opt_msg.setText(QCoreApplication.translate("MainWindow", "opt_msg", None))
        self.opt_triggers_btn.setText(QCoreApplication.translate("MainWindow", "Create Triggers", None))
        self.local_radio_btn.setText(QCoreApplication.translate("MainWindow", "Local", None))
        self.description_copy.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:700;">Copy the agent to the local or remote system.</span> Remember that the <span style=" font-style:italic;">python3</span>, <span style=" font-style:italic;">python3-pip</span> and <span style=" font-style:italic;">gunicorn</span> dependencies must be installed on the machine where the agent will run.</p></body></html>',
                None,
            )
        )
        self.remote_radio_btn.setText(QCoreApplication.translate("MainWindow", "Remote", None))
        self.groupBox.setTitle("")
        self.local_copy_btn.setText(QCoreApplication.translate("MainWindow", "Local WiPM copy", None))
        self.local_copy_msg.setText(QCoreApplication.translate("MainWindow", "local_copy_msg", None))
        self.ssh_user.setText(QCoreApplication.translate("MainWindow", "User", None))
        self.ssh_port.setText(QCoreApplication.translate("MainWindow", "Port", None))
        self.ssh_host_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "localhost", None))
        self.ssh_pass.setText(QCoreApplication.translate("MainWindow", "Password", None))
        self.ssh_host.setText(QCoreApplication.translate("MainWindow", "Hostname", None))
        self.ssh_port_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "22", None))
        self.ssh_upload_btn.setText(QCoreApplication.translate("MainWindow", "Upload WiPM agent", None))
        self.ssh_upload_msg.setText(QCoreApplication.translate("MainWindow", "ssh_msg", None))
        self.go_back_button.setText(QCoreApplication.translate("MainWindow", "Go back", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", "Next", None))
        self.powered_msg.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:700;">Powered by</span></p></body></html>',
                None,
            )
        )
        self.logo_footer.setText("")
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
