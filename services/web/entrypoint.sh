#!/bin/sh
export set FLASK_APP=__init__.py
python tom_db_manage.py create_db
exec "$@"
