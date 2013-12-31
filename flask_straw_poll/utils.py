# -*- coding: utf-8 -*-
"""Handy utility functions for flask-straw-poll
"""

from flask_straw_poll.models import Vote, Party, db
from flask.json import jsonify as _jsonify


def create_test_data():
    """Util function to create a set of parties and starting votes, to make
    both testing and demonstration simpler.
    """

    parties = (
        Party('Supercalifragilisticexpiallidocious party'),
        Party('Right-wingers party'),
        Party('That third lot party'),
        Party('We like puppies, lol, party')
    )
    for party in parties:
        db.session.add(party)
    db.session.commit()

    votes = (
        Vote(1, party=parties[0]),
        Vote(1, party=parties[0]),
        Vote(2, party=parties[0]),
        Vote(2, party=parties[1]),
        Vote(3, party=parties[1]),
        Vote(3, party=parties[1]),
        Vote(3, party=parties[3]),
        Vote(3, party=parties[3]),
        Vote(3, party=parties[2]),
    )
    for vote in votes:
        db.session.add(vote)
    db.session.commit()


def jsonify(obj=None, **kwargs):
    """Wrapper for Flask's jsonify util function to serialise simple SQLAlchemy
    models to JSON.
    """
    if isinstance(obj, db.Model):
        kwargs = {}
        for c in obj.__table__.columns:
            kwargs[c.name] = getattr(obj, c.name)

    return _jsonify(**kwargs)
