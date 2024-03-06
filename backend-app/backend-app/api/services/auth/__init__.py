from flask import Blueprint
from api.services.auth import routes

auth_bp = Blueprint('auth', __name__)
