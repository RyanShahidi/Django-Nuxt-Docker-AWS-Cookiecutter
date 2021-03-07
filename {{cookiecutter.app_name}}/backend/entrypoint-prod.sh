#!/bin/sh
python manage.py migrate
python manage.py createsu
python manage.py collectstatic --no-input --clear

exec gunicorn backend.wsgi:application --bind 0.0.0.0:1339