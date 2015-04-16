#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SelectField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange


class RegisterForm(Form):
    days = [('0', u'Día')]
    for i in range(1, 32):
        days.append((i, i))

    months = [('0', u'Mes')]
    for i in range(1, 13):
        months.append((i, i))

    years = [('0', u'Año')]
    for i in range(2014, 1914, -1):
        years.append((i, i))

    name = StringField('name', validators=[DataRequired(message=u'Nombre requerido.')])
    middleName = StringField('lastName')
    lastName = StringField('lastName', validators=[DataRequired(message=u'Apellido requerido.')])

    codeArea = IntegerField('codeArea', validators=[DataRequired(message=u'Lada requerida.'),
                                                    NumberRange(min=10, max=999,
                                                                message=u'Se requiere un código de área válido.')])

    telephone = IntegerField('telephone', validators=[DataRequired(message=u'Teléfono requerido.'),
                                                      NumberRange(min=1000000, max=99999999,
                                                                  message=u'Se requiere un teléfono válido.')])

    mail = EmailField('mail', validators=[DataRequired(message=u'Correo electrónico requerido.'),
                                          EqualTo('confirmMail', message=u'Confirma el correo electrónico.'),
                                          Email(message=u'Formato de correo inválido.')])

    confirmMail = EmailField('mail', validators=[Email(message=u'Formato de correo inválido.')])

    prefix = SelectField('prefix', validators=[DataRequired(message=u'Título requerido.')],
                         choices=[('-', u'Seleccione ...'), ('Srita.', 'Srita.'), ('Sra.', 'Sra.'),
                                  ('Sr.', 'Sr.')])
    gender = SelectField('gender', validators=[DataRequired(message=u'Género requerido.')],
                         choices=[('-', u'Seleccione ...'), ('F', u'Femenino'), ('M', u'Masculino')])

    nationality = SelectField('nationality', validators=[DataRequired(message=u'Nacionalidad requerida.')],
                              choices=[('-', u'Seleccione ...'), ('Mexico', u'México'),
                                       ('USA', u'USA'), ('Otra', u'Otra')])

    birthDay = SelectField('birthDay', coerce=int, validators=[DataRequired(message=u'Día requerido.'),
                                                               NumberRange(min=1, max=31, message=u'Día inválido.')],
                           choices=days)
    birthMonth = SelectField('birthMonth', coerce=int, validators=[DataRequired(message=u'Mes requerido.'),
                                                                   NumberRange(min=1, max=12,
                                                                               message=u'Mes inválido.')],
                             choices=months)
    birthYear = SelectField('birthYear', coerce=int, validators=[DataRequired(message=u'Año requerido.'),
                                                                 NumberRange(min=1914, max=2014,
                                                                             message=u'Año inválido.')], choices=years)