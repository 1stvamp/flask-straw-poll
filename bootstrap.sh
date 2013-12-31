#!/bin/bash
echo 'Getting WMC data from mapit.mysociety.org..'
curl http://mapit.mysociety.org/areas/WMC -o data/wmc.json
echo 'Setting up venv..'
virtualenv --no-site-packages ./venv
source ./venv/bin/activate
echo 'Installing requirements..'
pip install -r requirements.txt
echo 'Creating DB models..'
python -c 'from flask_straw_poll.models import main; main()'
echo 'Creating test data (parties)..'
python -c 'from flask_straw_poll.utils import create_test_data; create_test_data()'
echo 'Done.'
