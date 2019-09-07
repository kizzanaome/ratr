from flask import Flask, abort, make_response, Response, jsonify
from models import User, db
from flask_restful import Api, Resource, fields, reqparse
import json
from sqlalchemy import exc


class AllUsers(Resource):
    def get(self):
        users = User.query.all()
        users = [user.serialize(exclude=['password']) for user in users]
        return jsonify(data=users)


class CreteAccount(Resource):
    """Resource for creating an account"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username')
        self.reqparse.add_argument('password')

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username']
        password = args['password']
        user = User(username=username, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            return make_response(
                {"message": "Your account has been created succesfully"}, 201)
        except exc.IntegrityError:
            db.session.rollback()
            check_user = user.query.filter_by(username=username).first()
            if check_user:
                return make_response({"message": "User already exists"}, 403)


class Login(Resource):
    def post(self):
        req = reqparse.RequestParser()
        req.add_argument('username')
        req.add_argument('password')
        args = req.parse_args()
        username = args['username']
        password = args['password']
        user = User.query.filter_by(username=username).first()


# api.add_resource(CreteAccount, '/api/signup')
# api.add_resource(Login, '/api/login')
