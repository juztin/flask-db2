Changelog
=========

.. currentmodule:: Flask-DB2

Release 0.0a10
-------------

Wrapping connection.close with a try/except to avoid blow-ups.

Release 0.0a9
-------------

Revisits BUGFIX #4 - another Windows `lf+cr` issue.

Release 0.0a8
-------------

BUGFIX #4 - Resolves an issue where on Windows the error message was including `lf+cr`
            and the RegEx wasn't catching this.

Release 0.0a7
-------------

Added try_parse method to DB2Error.

Release 0.0a6
-------------

Added DB2Error class to handle parsing out error codes/message.

Release 0.0a5
-------------

Checking for None type cursor/row in row_factory and returning None.

Release 0.0a4
-------------

Added example.py
Added optional mapper object to convert column names to custom
  values in row_factory

Release 0.0a3
-------------

Added config keyword arg to connect function, for custom connections.

Release 0.0a2
-------------

Fixed accessing the context for the database when the context is None.

Release 0.0a1
-------------

Initial release
