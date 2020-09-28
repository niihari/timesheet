from control.validation.validation_base import ValidationError
from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy


class APIHelper:

    api_manager: APIManager = None

    @staticmethod
    def add_api(model_class):

        APIHelper.api_manager.create_api(model_class, methods=['GET', 'POST', 'DELETE'], validation_exceptions=[ValidationError])

    @staticmethod
    def create_api(app: Flask, db: SQLAlchemy):

        APIHelper.api_manager = APIManager(app, flask_sqlalchemy_db=db)