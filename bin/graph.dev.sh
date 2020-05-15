#!/bin/bash

export GRAPH_BIN_DIR=$(dirname $(realpath "$0"))
export GRAPH_ABSOULUTE_ROOT_DIR="$( dirname "$GRAPH_BIN_DIR" )"

function grapphin() {
    cmd=$1
    $GRAPH_BIN_DIR/graph.$cmd.sh "${@:2}"
}

GRAPPHIN_VENV="gvenv"
GRAPH_ROOT_DIR=$(realpath --relative-to="$PWD" ${GRAPH_ABSOULUTE_ROOT_DIR})
GRAPH_VENV_DIR="$GRAPH_ROOT_DIR/$GRAPPHIN_VENV"

if [ ! -d $GRAPH_VENV_DIR ]
then
    python3 -m venv $GRAPH_VENV_DIR
fi

source $GRAPH_ROOT_DIR/.env
source "$GRAPH_VENV_DIR/bin/activate"
