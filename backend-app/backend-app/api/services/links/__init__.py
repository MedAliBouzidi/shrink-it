from flask import Blueprint
from api.services.links import routes

links_bp = Blueprint('links', __name__)
