import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

load_dotenv() 

def mysql_uri() -> str:
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    name = os.getenv("DB_NAME", "notes")

    return(f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}")

class config:
    SQLALCHEMY_DATABASE_URI = mysql_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def db_connection():
    uri = config.SQLALCHEMY_DATABASE_URI

    try:
        engine = create_engine(uri)
        conection = engine.connect()
        print("Database connected")
        conection.close()
        return True
    except OperationalError as e:
        raise Exception(f"Database connection failed: {e}")   