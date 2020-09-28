from control.api.api_utils import APIHelper
from control.app import app_utils
from control.validation.validation_base import ValidationError
from sqlalchemy import Column, String, TIMESTAMP, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, validates
from typing import Union, Tuple
from validate_docbr import CPF
from validate_email import validate_email


class Colaborador(app_utils.db.Model):

    cpf = Column(String(11), nullable=False, primary_key=True)
    nome = Column(String(50), nullable=False)
    prenome = Column(String(50), nullable=True)
    sobrenome = Column(String(50), nullable=False)
    cargo = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    data_nascimento = Column(TIMESTAMP, nullable=False)
    email = Column(String(50), nullable=False)
    endereco = Column(String(50), nullable=False)
    numero = Column(String(50), nullable=False)
    complemento = Column(String(50), nullable=True)
    bairro = Column(String(50), nullable=False)
    cidade = Column(String(50), nullable=False)
    estado = Column(String(50), nullable=False)
    cep = Column(String(8), nullable=False)
    ddd = Column(String(2), nullable=False)
    telefone = Column(String(9), nullable=False)
    pontos = relationship('Ponto', cascade="all,delete", backref='colaborador', lazy=True)

    @validates('cpf')
    def validate_cpf(self, key, value: Union[str, Tuple]):

        cpf = CPF()

        if type(value) is tuple:
            value = value[0]

        if not cpf.validate(value):
            exception = ValidationError()
            exception.errors = dict(cpf='Please try again with a valid CPF')
            raise exception

        return value

    @validates('email')
    def validate_email(self, key, value: Union[str, Tuple]):

        if type(value) is tuple:
            value = value[0]

        if not validate_email(value):
            exception = ValidationError()
            exception.errors = dict(email='Please try again with a valid E-mail')
            raise exception

        return value


class Ponto(app_utils.db.Model):

    id = Column(Integer, primary_key=True)
    data_hora = Column(TIMESTAMP, nullable=False)
    cpf_colaborador = Column(String(11),
                             ForeignKey('colaborador.cpf', ondelete='CASCADE'),
                             nullable=False)


APIHelper.add_api(Colaborador)
APIHelper.add_api(Ponto)