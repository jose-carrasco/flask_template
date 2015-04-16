#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import db
from src.helpers import encrypt
from datetime import datetime


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(10))
    name = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    gender = db.Column(db.String(1))
    nationality = db.Column(db.String(50))
    codeArea = db.Column(db.String(3))
    telephone = db.Column(db.String(10))
    email = db.Column(db.String(100))
    birthday = db.Column(db.DateTime)
    uuid = db.Column(db.String(100))
    enabled = db.Column(db.Boolean)
    registerDate = db.Column(db.DateTime)

    def __init__(self, prefix, name, middleName, lastName, gender, birthday, nationality, codeArea, telephone, email):
        self.prefix = prefix
        self.name = name
        self.middleName = middleName
        self.lastName = lastName
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.nationality = nationality
        self.codeArea = codeArea
        self.telephone = telephone
        self.registerDate = datetime.now()
        self.enabled = True
        self.uuid = encrypt(str(email) + str(lastName) + str(name))

    def send_mail(self):
        import smtplib
        from flask import render_template
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from config import EMAIL_SENDER, MAIL_SENDER_PASSWORD, MAIL_SENDER_USER

        msg = MIMEMultipart('alternative')

        msg['Subject'] = u"subject"
        msg['From'] = EMAIL_SENDER
        msg['To'] = self.email

        html = render_template('mailing/mailing.html', name=self.name + " " + self.lastName)

        part2 = MIMEText(html.encode('utf-8'), 'html', 'utf-8')

        msg.attach(part2)

        s = smtplib.SMTP('smtp.mandrillapp.com', 587)

        s.login(MAIL_SENDER_USER, MAIL_SENDER_PASSWORD)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

    def __repr__(self):
        return '<Winner %r %r>' % self.name % self.lastName