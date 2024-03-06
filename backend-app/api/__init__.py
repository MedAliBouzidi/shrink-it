"""
    Description: This file is the main file of the API, here we define the app and the database connection.
"""
# Libraries
from flask import Flask
from flask_cors import CORS
from mongoengine import MongoEngine

# Services and Routes Blueprints
from api.services.auth import auth_bp
from api.services.links import links_bp
from api.services.users import users_bp

# Config
from api.config import config

app = Flask(__name__)
app.config['MONGO_URI'] = config['MONGO_URI']
app.config.from_object(config)
app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
app.register_blueprint(links_bp, url_prefix='/api/v1/links')
app.register_blueprint(users_bp, url_prefix='/api/v1/users')

CORS(app)
mongodb = MongoEngine(app)
