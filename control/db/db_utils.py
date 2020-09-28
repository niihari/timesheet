from constants.defines import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_INSTANCE
from flask_sqlalchemy import SQLAlchemy


def create_db(db: SQLAlchemy):

    db.create_all()


def db_string():

    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_INSTANCE}"