from flask import Blueprint
from .Signin import signin

api = Blueprint('api', __name__)

@api.route('/signin', methods=['POST'])
def signin():
    return signin()

