Flask-DB2
=========

`Flask-DB2`_ is an extension to `Flask`_ that uses the ibm_db_dbi
driver for database connections.

::

    from flask import Flask
    from flask_db2 import DB2

    app = Flask(__name__)
    db = DB2(app)


    @app.route('/')
    def index()
        cur = db.connection.cursor()
        cur.execute(...)


get Flask-DB2
=============

Install `flask`_

    sudo easy_install Flask-DB2

Download the latest release from `Python Package Index`_
or clone `the repository`_

.. _Flask-DB2:  http://packages.python.org/Flask-DB2
.. _Flask: http://flask.pocoo.org/
.. _the repository: https://github.com/juztin/flask-db2
.. _Python Package Index: https://pypi.python.org/pypi/Flask-DB2
