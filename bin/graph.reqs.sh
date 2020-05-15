#!/bin/bash

GRAPH_ROOT_DIR=$(realpath --relative-to="$PWD" ${GRAPH_ABSOULUTE_ROOT_DIR})

pip-compile -q --allow-unsafe --output-file "$GRAPH_ROOT_DIR/requirements.dev.txt" "$GRAPH_ROOT_DIR/setup/requirements.dev.in"
pip-compile -q --allow-unsafe --output-file "$GRAPH_ROOT_DIR/requirements.txt" "$GRAPH_ROOT_DIR/setup/requirements.prod.in"
