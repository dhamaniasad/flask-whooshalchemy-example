from app import app, db
import datetime
import flask.ext.whooshalchemy as whooshalchemy

class Post(db.Model):
    __tablename__ = 'posts'
    __searchable__ = ['text', 'title']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    text = db.Column(db.Text)
    added_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, title, text):
        self.title = title
        self.text = text


whooshalchemy.whoosh_index(app, Post)
