# -*- coding: utf-8 -*-
"""Database models for flask-straw-poll
"""
from __future__ import print_function

from sys import stdout, exit
from flask.ext.sqlalchemy import SQLAlchemy

from flask_straw_poll import app

db = SQLAlchemy(app)


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)

    def __init__(self, name):
        self.name = name
        super(Party, self).__init__()


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    party = db.relationship('Party', backref=db.backref('party',
                            lazy='dynamic'))
    constituency_id = db.Column(db.Integer)

    def __init__(self, constituency_id, party=None, party_id=None):
        self.constituency_id = int(constituency_id)

        if party_id is not None:
            self.party_id = int(party_id)
        if party is not None:
            self.party = party
            self.party_id = party.id

        if not self.party_id:
            raise ValueError('party_id or party argument missing')

        super(Vote, self).__init__()


def main():
    print('Creating database elements with URI "{0}"..'.format(
            app.config['SQLALCHEMY_DATABASE_URI']), file=stdout)

    try:
        db.create_all()
    except Exception as e:
        print(e, file=stderr)
        return 1
    else:
        return 0

if __name__ == '__main__':
    exit(main())
