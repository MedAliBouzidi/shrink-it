"""
    This file contains the User model.
    The User model is responsible for handling the user data.
"""
from datetime import datetime
from bson import ObjectId
from mongoengine import Document, StringField, DateTimeField


class User(Document):
    """
        User model class
    """
