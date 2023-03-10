#!/bin/sh

echo "Waiting for postgres..."

echo "database started"


python manage.py migrate


python manage.py flush --noinput
python manage.py loaddata dummy_data.json

python manage.py runserver 0.0.0.0:8000
