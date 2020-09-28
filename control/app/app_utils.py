from control.api.api_utils import APIHelper
from control.db.db_utils import db_string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_string()
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

APIHelper.create_api(app=app, db=db)