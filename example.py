#!/usr/bin/env python

import simplejson as json
import datetime
import decimal

from flask import Flask
from flask.ext.db2 import DB2

app = Flask(__name__)
db = DB2(app)

mapper = {
    "00001": "serverName",
    "00002": "serverTime",
}


date_handler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime)
    or isinstance(obj, datetime.date)
    else None
)


@app.route('/')
def index():
    cur = db.connection.cursor()
    cur.execute("SELECT user, current timestamp FROM sysibm.sysdummy1")
    row = cur.fetchone()
    data = db.row_factory(cur, row, mapper=mapper)
    cur.close()

    return json.dumps(data, indent=4, separators=(',', ': '), default=date_handler)

app.run(host="0.0.0.0", debug=True)
