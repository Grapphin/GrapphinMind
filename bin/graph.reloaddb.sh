#!/bin/bash


GRAPH_ROOT_DIR=$(realpath --relative-to="$PWD" ${GRAPH_ABSOULUTE_ROOT_DIR})
DJANGO_ROOT_DIR="$GRAPH_ROOT_DIR/grapphin"

DB_FOLDER="$DJANGO_ROOT_DIR/db"
DB_NAME="db.sqlite3"

rm "$DB_FOLDER/$DB_NAME"

python "$DJANGO_ROOT_DIR/manage.py" makemigrations
python "$DJANGO_ROOT_DIR/manage.py" migrate
python "$DJANGO_ROOT_DIR/manage.py" loaddata $DB_FOLDER/fixtures/*
