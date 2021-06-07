#!/bin/sh
set -e

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
	python manage.py makemigrations
    python manage.py migrate
fi

python manage.py runserver 0.0.0.0:8000
exec "$@"