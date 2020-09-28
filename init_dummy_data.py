from dateparser import parse as parse_date
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from model.models import Colaborador, Ponto
from random import randrange
from validate_docbr import CPF


def random_date(start, end):

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def init_dummy_data(db: SQLAlchemy):

    cpf = CPF()
    generated_cpf = cpf.generate()
    d1 = parse_date(u'1900/01/01 00:00:00')
    d2 = parse_date(u'2020/01/01 23:59:59')

    me = Colaborador()

    me.cpf = generated_cpf,
    me.nome = 'John',
    me.prenome = '',
    me.sobrenome = 'Smith',
    me.cargo = 'Functional Test Engineer',
    me.status = 'Ativo',
    me.data_nascimento = random_date(d1, d2),
    me.email = 'abc@cde.com',
    me.endereco = 'Rua Um Dois Três Quatro',
    me.numero = '567',
    me.complemento = 'ap 890',
    me.bairro = 'Fixe Giro',
    me.cidade = 'São Paulo',
    me.estado = 'SP',
    me.cep = '00000000',
    me.ddd = '11',
    me.telefone = '987654321'

    db.session.add(me)
    db.session.commit()

    mi = Ponto()

    mi.data_hora = random_date(d1, d2)
    mi.cpf_colaborador = generated_cpf

    db.session.add(mi)
    db.session.commit()