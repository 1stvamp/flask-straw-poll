# -*- coding: utf-8 -*-
"""View handlers/controllers and URL routing for flask-straw-poll
"""

from sqlalchemy import desc, func
from flask import session, request, render_template

from flask_straw_poll import app
from flask_straw_poll.models import db, Party, Vote
from flask_straw_poll.utils import jsonify

@app.context_processor
def inject_wmc_data():
    return {'wmc_data': app.WMC_DATA}


@app.route('/')
def home():
    context = {}
    context['parties'] = Party.query.all()
    context['party_votes'] = db.session.query(
                                    func.count('*'),
                                    Party.name) \
                                .select_from(Vote) \
                                .join(Party) \
                                .group_by(Vote.party_id) \
                                .order_by(desc('count_1')).all()
    context['total_votes'] = Vote.query.count()

    context['constituency_votes'] = db.session.query(
                                    func.count('*'),
                                    Vote.constituency_id) \
                                .group_by(Vote.constituency_id) \
                                .order_by(desc('count_1')).all()

    return render_template('index.html', **context)


@app.route('/votes/', methods=['POST'])
def create_vote():
    if session.get('voted'):
        return jsonify(error='Already voted.'), 401

    vote = Vote(constituency_id=request.form.get('constituency_id'),
                party_id=request.form.get('party_id'))
    db.session.add(vote)
    db.session.commit()

    session['voted'] = True

    return jsonify(vote)
