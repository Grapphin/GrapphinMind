#!/bin/bash

GRAPH_ROOT_DIR=$(realpath --relative-to="$PWD" ${GRAPH_ABSOULUTE_ROOT_DIR})
DJANGO_ROOT_DIR="$GRAPH_ROOT_DIR/grapphin"

python "$DJANGO_ROOT_DIR/manage.py" "$@"
