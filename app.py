from control.api.consulta_horas import register_consulta_horas
from control.app.app_utils import app, db
from control.db.db_utils import create_db
from constants.defines import API_PORT
from flask import Flask


def run_app(app: Flask, port):

    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':

    from init_dummy_data import init_dummy_data

    create_db(db=db)

    init_dummy_data(db=db)
    register_consulta_horas(app=app)

    run_app(app=app, port=API_PORT)