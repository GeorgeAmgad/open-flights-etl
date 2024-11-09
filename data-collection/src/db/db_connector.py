import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import os

DB_USER = 'DB_USER'

DB_NAME = 'DB_NAME'

DB_PORT = 'DB_PORT'

DB_HOST = 'DB_HOST'

DB_PASSWORD = 'DB_PASSWORD'

load_dotenv()


def get_db_connection():
    """Establish a connection to the PostgreSQL database using environment variables."""
    try:
        connection = psycopg2.connect(
            host=os.getenv(DB_HOST),
            port=os.getenv(DB_PORT),
            database=os.getenv(DB_NAME),
            user=os.getenv(DB_USER),
            password=os.getenv(DB_PASSWORD)
        )
        return connection
    except Exception as e:
        print("Error connecting to the PostgreSQL database:", e)
        return None


def get_db_engine():
    """Establish a connection to the PostgreSQL database and return an SQLAlchemy engine."""
    try:
        db_url = URL.create(
            drivername="postgresql+psycopg2",
            username=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        return create_engine(db_url)
    except Exception as e:
        print("Error creating the SQLAlchemy engine:", e)
        return None


def get_postgres_version():
    """Retrieve and print the PostgreSQL database version."""
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print("PostgreSQL version:", version[0])
    except Exception as e:
        print("Error executing query:", e)
    finally:
        cursor.close()
        connection.close()
        print("Database connection closed.")
