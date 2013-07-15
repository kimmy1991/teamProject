import datetime
from flask import url_for
from appstore import db


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    category = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    # comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    # def get_absolute_url(self):
    #     return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name

    # meta = {
    #     'allow_inheritance': True,
    #     'indexes': ['-created_at', 'slug'],
    #     'ordering': ['-created_at']
    # }


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=25, required=True, unique=True)
    password = db.StringField(max_length=30, required=True)
    email = db.StringField(max_length=30, required=True, unique=True)    