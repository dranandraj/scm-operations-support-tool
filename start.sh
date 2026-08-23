#!/bin/bash

echo "Starting PostgreSQL..."

if docker ps --format '{{.Names}}' | grep -q "^scm-postgres$"; then
    echo "PostgreSQL is already running."
elif docker ps -a --format '{{.Names}}' | grep -q "^scm-postgres$"; then
    docker start scm-postgres
    echo "PostgreSQL container started."
else
    echo "scm-postgres container not found."
    echo "Please create the database container first."
    exit 1
fi

echo "Starting Flask application..."
python app.py
