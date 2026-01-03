import os
from dotenv import load_dotenv
from urllib.parse import quote_plus  # this encodes special chars in password

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # URL-encode the password automatically
    encoded_password = quote_plus(DB_PASSWORD)

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
