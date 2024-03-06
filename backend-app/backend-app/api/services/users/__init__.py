from flask import Blueprint
from api.services.users import routes

users_bp = Blueprint('users', __name__)