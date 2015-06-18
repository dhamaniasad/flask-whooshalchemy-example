from models import Post
import flask.ext.whooshalchemy as whooshalchemy
from app import app


def rebuild_index(model):
    primary_field = model.pure_whoosh.primary_key_name
    searchables = model.__searchable__
    index_writer = whooshalchemy.whoosh_index(app, model)

    query = model.query.all()
    with index_writer.writer() as writer:
        for post in query:
            index_attrs = {}
            for field in searchables:
                index_attrs[field] = unicode(getattr(post, field))
            index_attrs[primary_field] = unicode(getattr(post, primary_field))
            writer.update_document(**index_attrs)

rebuild_index(Post)
