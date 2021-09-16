from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument("email", type=str, required=True, help="Please input email")
parser.add_argument("username", type=str, required=True, help="Please input username")


class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        email = args["email"]
        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]

        newUser = UserModels(username, email, password, confirm_password)
        newUser.save_user()

        return {
            "message": "User registered successfully",
            "user": newUser.__dict__,
        }, 201

    def get(self):

        return {
            "user": UserModels.users,
        }


class UserSearch(Resource):
    def get(self, id):
        user_id = int(id) - 1

        return {
            "user": UserModels.users[user_id],
        }
