import os
import json
import tempfile
import unittest

from straw_poll_tests_config import TestConfig

os.environ['STRAW_POLL_CONFIG_OBJECT'] = 'straw_poll_tests_config.TestConfig'
DB_FD, DB_FILENAME = tempfile.mkstemp()
# The sqlite3 lib will handle the file descriptor, we just want the temp
# filename
os.close(DB_FD)

TestConfig.SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % (DB_FILENAME,)

import flask_straw_poll


class StrawPollTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_straw_poll.app
        self.client = self.app.test_client()
        flask_straw_poll.models.db.create_all()
        flask_straw_poll.utils.create_test_data()

        self.app.WMC_DATA = {
            u'1': {u'name': u'Downtroddenville'},
            u'2': {u'name': u'Upper Grass-Green'},
            u'3': {u'name': u'Somewhere else'}
        }

    def tearDown(self):
        os.unlink(DB_FILENAME)

    def test_parties_present_on_home(self):
        response = self.client.get('/')
        assert 'Supercalifragilisticexpiallidocious party' in response.data
        assert 'Right-wingers party' in response.data
        assert 'That third lot party' in response.data
        assert 'We like puppies, lol, party' in response.data

    def test_create_vote_api(self):
        response = self.client.post('/votes/', data={
                            'constituency_id': 3,
                            'party_id': 1
                        })
        data = json.loads(response.data)
        assert 'id' in data
        assert data['constituency_id'] == 3
        assert data['party_id'] == 1

    def test_constituences_rendered(self):
        response = self.client.get('/')
        assert str(self.app.WMC_DATA.values()[0]['name']) in response.data

    def test_you_only_vote_once_mr_bond(self):
        response = self.client.get('/')
        assert 'Cast your vote' in response.data

        response = self.client.post('/votes/', data={
                            'constituency_id': 2,
                            'party_id': 1
                        })
        assert response.status_code == 200

        response = self.client.get('/')
        assert 'Cast your vote' not in response.data

        response = self.client.post('/votes/', data={
                            'constituency_id': 2,
                            'party_id': 1
                        })
        assert response.status_code == 401



if __name__ == '__main__':
    unittest.main()
