# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, json
from flask.ext import restful
from src import db
from models import User


services = Blueprint('services', __name__)


class UsersRest(restful.Resource):
    def get(self):
        result = {}
        try:
            users = db.session.query(User.name, User.lastName, User.email).filter(User.enabled == 1).all()
            print users
            if users is not None:
                users_parsed = []
                for user in users:
                    user_parsed = {"complete_name": user[0] + " " + user[1], "email": user[2]}
                    users_parsed.append(user_parsed)
                result['status'] = 1
                result['data'] = users_parsed
            else:
                result['status'] = 0
                result['dat'] = u"No users"

            return json.dumps(result)
        except Exception, e:
            from helpers import validate_db
            result['status'] = 0
            result['message'] = u"Unexpected error: " + validate_db(str(e))[:50]
            return json.dumps(result)


api = restful.Api(services)
api.add_resource(UsersRest, '/services/users')