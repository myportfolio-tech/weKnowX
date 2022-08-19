#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"
echo "Starting Flask"

python manage.py run -h 0.0.0.0