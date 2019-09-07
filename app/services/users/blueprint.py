from flask import Blueprint
from flask_restful import Api

from views import CreteAccount, Login, AllUsers

users = Blueprint('users', __name__, url_prefix='/api/v1')

user_api = Api(users)

user_api.add_resource(CreteAccount, '/auth/signup')
user_api.add_resource(Login, '/auth/login')
user_api.add_resource(AllUsers, '/users')
