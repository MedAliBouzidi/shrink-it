"""
    This file contains the Link model.
    The Link model is responsible for handling the link data.
"""
from datetime import datetime
from mongoengine import StringField, Document

from api.models.user import User


class Link(Document):
    """
    Link model class
    """
    # link model fields
    long_link = StringField(required=True)
    short_link = StringField(required=True)
    created_at = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user = StringField(required=True)

    # link model meta data
    meta = {
        'collection': 'links'
    }
