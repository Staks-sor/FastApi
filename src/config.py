from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DB_HOST_TEST = os.environ.get("DB_HOST")
DB_PORT_TEST = os.environ.get("DB_PORT")
DB_NAME_TEST = os.environ.get("DB_NAME")
DB_USER_TEST = os.environ.get("DB_USER")
DB_PASS_TEST = os.environ.get("DB_PASS")

SECRET_AUTH = os.environ.get("SECRET_AUTH")

SMTP_USER = os.environ.get("SECRET_USER_MAIL")
SMTP_PASSWORD = os.environ.get("SECRET_USER_CODE")
