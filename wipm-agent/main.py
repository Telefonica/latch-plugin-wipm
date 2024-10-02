import os
import sys
import hmac
import time
import base64
import hashlib
import threading
from contextlib import asynccontextmanager
from datetime import datetime, timedelta

import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, Depends, Header
from fastapi.responses import PlainTextResponse
from latch import Latch

load_dotenv()

LATCH_APP_ID = os.environ.get("LATCH_APP_ID")
LATCH_SECRET_KEY = os.environ.get("LATCH_SECRET_KEY")
LATCH_ACCOUNT_ID = os.environ.get("LATCH_ACCOUNT_ID")
LATCH_READ_ONLY_OP = os.environ.get("LATCH_READ_ONLY_OP")
LATCH_EDITION_OP = os.environ.get("LATCH_EDITION_OP")
LATCH_ADMIN_OP = os.environ.get("LATCH_ADMINISTRATION_OP")

DB_CONFIG = {
    "user": "root",
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "database": os.environ.get("DB_NAME"),
}

LATCHES = ["ReadOnly", "Edition", "Administration"]

cnx = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global cnx
    cnx = connect_to_mysql(DB_CONFIG, attempts=3)
    if cnx is None:
        sys.exit(1)
    notification_thread = threading.Thread(target=check_notifications, daemon=True)
    notification_thread.start()
    yield
    pass


app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None)


def connect_to_mysql(config, attempts=3, delay=2):
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if attempts is attempt:
                # Attempts to reconnect failed; returning None
                print(f"Failed to connect, exiting without a connection: {err}")
                return None
            print(f"Connection failed: {err}. Retrying ({attempt}/{attempts - 1})...")
            # progressive reconnect delay
            time.sleep(delay**attempt)
            attempt += 1
    return None


def execute_query(query: str, params: tuple = None):
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            cursor.execute(query, params)
            cnx.commit()


def fetch_query(
    query: str,
    params: tuple = None,
):
    if cnx and cnx.is_connected():
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()


async def verify_signature(request: Request, x_11paths_authorization: str = Header(...)) -> None:
    body = await request.body()
    signature = base64.b64encode(hmac.new(LATCH_SECRET_KEY.encode(), body, hashlib.sha1).digest()).decode().rstrip()

    if signature != x_11paths_authorization:
        raise HTTPException(status_code=401, detail="Invalid signature")


def send_notification():
    latch_instance = Latch(LATCH_APP_ID, LATCH_SECRET_KEY)
    latch_instance.operation_status(LATCH_ACCOUNT_ID, LATCH_READ_ONLY_OP)
    latch_instance.operation_status(LATCH_ACCOUNT_ID, LATCH_EDITION_OP)
    latch_instance.operation_status(LATCH_ACCOUNT_ID, LATCH_ADMIN_OP)


def check_notifications():
    last_notification = None
    while True:
        try:
            results = fetch_query(
                "SELECT * FROM mysql.general_log WHERE argument REGEXP 'SIGNAL SQLSTATE \\'45000\\'.*' ORDER BY event_time DESC LIMIT 1",
            )

            current_time = datetime.now()
            if results:
                result_time = results[0]["event_time"]

                if last_notification is not None:
                    if current_time - last_notification > timedelta(seconds=30) and result_time - last_notification > timedelta(seconds=30):
                        last_notification = result_time
                        send_notification(result_time)
                else:
                    if current_time - result_time <= timedelta(seconds=30):
                        last_notification = result_time
                        send_notification(result_time)

            execute_query("SET GLOBAL general_log=0;")
            execute_query("TRUNCATE table mysql.general_log;")
            execute_query("SET GLOBAL general_log=1;")
            execute_query("SET GLOBAL log_output='TABLE';")

        except Exception as e:
            print(f"Error in check_notifications: {e}")

        time.sleep(3)


@app.get("/ping", response_class=PlainTextResponse)
async def ping_health():
    return "pong"


@app.get("/hook", response_class=PlainTextResponse)
async def verify_challenge(challenge: str):
    """
    Webhook challenge verification endpoint.
    """
    return challenge


@app.post("/hook")
async def receive_notification(request: Request, verified: None = Depends(verify_signature)):
    """
    Webhook notification endpoint.
    """
    body_json = await request.json()

    for account in body_json.get("accounts", {}).values():
        for latch in account:
            latch_id = latch["id"]
            latch_status = latch["new_status"]

            if latch_id in ("GLOBAL_LATCH", LATCH_APP_ID):
                print("Update all the table!")
                for latch_name in LATCHES:
                    execute_query("UPDATE latch.latch SET latch = %s WHERE operation_name = %s;", (latch_status, latch_name))
            else:
                print(f"Update specific latch in table ({latch_id}: {latch_status})")
                execute_query("UPDATE latch.latch SET latch = %s WHERE operation_id = %s;", (latch_status, latch_id))

        break

    return
