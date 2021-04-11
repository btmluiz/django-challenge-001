#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting database..."

    while [ ! nc -z $DJANGO_DATABASE_HOST 5432 ]; do
        sleep 0.1
    done

    echo "Database started"
fi

exec "$@"