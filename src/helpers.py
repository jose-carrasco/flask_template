#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from BeautifulSoup import BeautifulSoup


def encrypt(value):
    return hashlib.sha1(value.encode('utf-8')).hexdigest()


def validate_text(value):
    valid_tags = []
    soup = BeautifulSoup(value)
    for tag in soup.findAll(True):
        if tag.name not in valid_tags:
            tag.hidden = True

    return soup.renderContents()


def validate_db(value):
    if "MySQL" in str(value):
        return u"Error en la conexión con base de datos."
    if "Duplicate entry" in str(value):
        return u"El código ya fue asignado, intenta nuevamente."
    if "'email'" in str(value):
        return u"Existe un problema con tu cuenta de correo electrónico, por favor intenta nuevamente."
    return value


def datetime_utc_mexico():
    from datetime import datetime
    import pytz

    mexico = pytz.timezone('America/Mexico_City')
    date = datetime.now(pytz.utc)
    return datetime.astimezone(date, mexico)


def datetime_to_utc_mexico(date):
    import pytz

    mexico = pytz.timezone('America/Mexico_City')
    return mexico.localize(date)


def is_email(email):
    from lepl.apps.rfc3696 import Email

    validator = Email()
    if validator(email) is True:
        return email
    else:
        raise Exception(u"Cuenta de correo inválida.".encode('utf-8'))


def is_valid_string(value):
    if validate_string(value) is False:
        return value
    else:
        raise Exception(u"Dato inválido. ".encode('utf-8'))


def is_valid_number(value):
    if value.isdigit():
        return value
    else:
        raise Exception(u"Dato inválido.".encode('utf-8'))


def validate_string(value):
    return any(char.isdigit() for char in value)


def is_valid_age(value):
    from datetime import date

    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age >= 18 and age < 100:
        return value
    else:
        raise Exception(u"El registro solo es para mayores de edad.".encode('utf-8'))
