flask-straw-poll
================

Example straw poll Flask app


UK Parliament constituency data
-------------------------------

This app requires area data in the format:


.. code-block:: json
    
    {
      "id": { "name": "Placename" }
    {

It was developed with Westminster Constituency data freely available from mapit.mysociety.org
(under the terms of the `OS OpenData license <http://www.ordnancesurvey.co.uk/oswebsite/opendata/licence/>`_ and the `Open Government License <http://www.nationalarchives.gov.uk/doc/open-government-licence/open-government-licence.htm>`_).

You can either create your own data set under `./flask_straw_poll/data/wmc.json`, copy the example data from `./flask_straw_poll/data/wmc.json.example`, or download it from mapit:

.. code-block:: bash
    
    $ cd flask-straw-poll
    $ curl http://mapit.mysociety.org/areas/WMC -o flask_straw_poll/data/wmc.json
    
    $ # Or use the example data
    $ cp data/wmc.json.example data/wmc.json


Quick bootstrap script
----------------------

To get up and running with the demo quickly there is a bootstrap shell script which creates a virtualenv, installs the dependencies, downloads constituency data, creates the DB models in a local sqlite3 file, creates some test data, and copies the example config file to `config.json`:

.. code-block:: bash
    
    $ cd flack-straw-poll
    $ ./bootstrap.sh
    Getting WMC data from mapit.mysociety.org..
     [snip]
    
    Setting up venv..
     [snip]
    
    Installing requirements..
     [snip]

    Creating DB models..
     [snip]

    Creating test data (parties, votes)..
     [snip]

    Copying config.json.example -> config.json
    Done.

Usage
-----

To make quickly using the demo app faster (without setting up a WSGI serving env etc.) you can use the runserver script once all the depenencies, config and data are installed/in-place:

.. code-block:: bash

    $ cd flask-straw-poll
    $ python flask_straw_poll/runserver.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

You can then access the app in a browser via `127.0.0.1:5000 <http://127.0.0.1:5000/>`_.

You should see something like:

.. image:: https://f.cloud.github.com/assets/35831/1826756/3cc229d8-720c-11e3-9cac-8805ccba826d.png
