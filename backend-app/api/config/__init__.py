from datetime import timedelta
from os import environ
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

config = environ

MONGODB_USER = config.get('MONGODB_USER')
MONGODB_PASS = config.get('MONGODB_PASS')
MONGODB_DATABASE = config.get('MONGODB_DATABASE')
MONGODB_HOST = config.get('MONGODB_HOST')
MONGODB_PORT = config.get('MONGODB_PORT')

config['MONGO_URI'] = f'mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DATABASE}'

config['SECRET_KEY'] = config.get('SECRET_KEY')
config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30).__str__()
