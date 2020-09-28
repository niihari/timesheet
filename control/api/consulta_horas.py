from control.app.app_utils import db
from datetime import timedelta
from flask import Flask
from model.models import Colaborador, Ponto
from sqlalchemy import extract
from typing import List


def get_hours_from_delta(delta: timedelta):

    return delta.total_seconds()/3600


def calculate_hours(results: List[Colaborador]):

    pontos = sorted(results[0].pontos, key=lambda x: x.data_hora)

    ponto_entrada: Ponto
    ponto_saida: Ponto
    horas_dia = {

        ponto_entrada.data_hora.day: get_hours_from_delta(ponto_saida.data_hora - ponto_entrada.data_hora)
        for ponto_entrada, ponto_saida in zip(pontos[::2], pontos[1::2])

    }

    return horas_dia, sum(horas for horas in horas_dia.values())


def register_consulta_horas(app: Flask):

    @app.route('/api/consulta_horas/<colaborador>/<mes>/<ano>', methods=['GET'])
    def consulta_horas(colaborador, mes, ano):

        results: List[Colaborador] = db.session.query(Colaborador)\
                                               .join(Ponto)\
                                               .filter(Colaborador.cpf == colaborador)\
                                               .filter(extract('month', Ponto.data_hora) == mes)\
                                               .filter(extract('year', Ponto.data_hora) == ano)\
                                       .all()

        horas_dia, horas_mes = calculate_hours(results)

        return {
            'horas_dia': {key: "%.2f"%value for key, value in horas_dia.items()},
            'horas_mes': "%.2f" % horas_mes,
        }