#!/bin/bash

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --noinput

# loading english words to database
python manage.py loaddata --format=json Word.json


exec "$@"
