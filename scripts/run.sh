#!/bin/bash

set -e
set -x

/scripts/unpack_data.sh

#/bin/bash
THREADS=12 /run.sh run
