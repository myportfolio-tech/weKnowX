# users.pzy

from flask import Blueprint, request

from src import db
from src.api.models import User

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route("/users")
def users():

    post_data = request.get_json()
    username = post_data.get('username')
    email = post_data.get('email')
    response_object = {}
    
    user = User.query.filter_by(email=email).first()
    if user:
        response_object['message'] = 'Sorry. That email already exists.'
        return response_object, 400

    db.session.add(User(username=username, email=email))
    db.session.commit()

    response_object['message'] = f'{email} was added!'
    return response_object, 201