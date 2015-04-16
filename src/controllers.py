# !/usr/bin/env python
# -*- coding: utf-8 -*-

from forms import RegisterForm
from flask import Blueprint, render_template, request, flash
from src import db
from models import User
from helpers import is_valid_age, is_valid_string, is_valid_number, is_email

controllers = Blueprint('controllers', __name__)


@controllers.route('/')
def index():
    return render_template('home.html')


@controllers.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        import datetime

        birthday = is_valid_age(datetime.datetime.strptime(request.form['birthDay'] + "-" + request.form['birthMonth'] +
                                                           "-" + request.form['birthYear'], '%d-%m-%Y'))
        user_saved = User.query.filter_by(email=request.form['mail']).first()
        if user_saved is None:
            new_user = User(
                prefix=request.form['prefix'],
                name=is_valid_string(request.form['name']),
                middleName=is_valid_string(request.form['middleName']),
                lastName=is_valid_string(request.form['lastName']),
                gender=request.form['gender'],
                birthday=birthday,
                nationality=request.form['nationality'],
                codeArea=is_valid_number(request.form['codeArea']),
                telephone=is_valid_number(request.form['telephone']),
                email=is_email(request.form['mail'])
            )
            if new_user.prefix == "-" or new_user.gender == "-" or new_user.nationality == "-":
                raise Exception(u"Por favor, selecciona una opción válida.".encode('utf-8'))

            db.session.add(new_user)

            db.session.commit()
            return render_template('registered.html')
        else:
            flash(u'The user is already registered')
            return render_template('register.html', form=form)
    else:
        return render_template('register.html', form=form)


@controllers.route('/users', methods=['GET'])
def users():
    users = User.query.filter_by(enabled=True).all()
    return render_template('users.html', data=users)

@controllers.route('/users_via_restful', methods=['GET'])
def users_via_restful():
    return render_template('users_restful.html')