"""
    This file contains the Statistics model.
    The Statistics model is responsible for handling the statistics of a link.
"""
from datetime import datetime
from mongoengine import ObjectIdField, Document, DateTimeField, IntField


class Statistics(Document):
    """ Statistics model class """
    # statistics model fields
    link_visit_count = IntField(default=0)
    link = ObjectIdField(required=True)
    user = ObjectIdField(required=True)
    created_at = DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # statistics model meta data
    meta = {'collection': 'statistics'}

    def __init__(self, link, user, *args, **values):
        super().__init__(*args, **values)
        self.link = link
        self.user = user

    def get_statistics(self, link_id):
        """
        Get the statistics of a link
        :param link_id: The link identifier
        :return: The statistics of the link
        """
        return None
