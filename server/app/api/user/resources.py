from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt

from app.api.user.models import User
from app.security import TokenBlacklist


class UserRegisterApi(Resource):
    def post(self):
        pass
class UserLoginApi(Resource):
    def post(self):
        pass
class UserLogoutApi(Resource):
    @jwt_required
    def post(self):
        pass
class UserApi(Resource):
    @jwt_required
    def get(self):
        pass