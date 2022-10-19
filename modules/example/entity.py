from db import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    """This is model for create table"""
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True,index=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self,id, url, result_all, result_no_stop_words):
        self.id = id
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)