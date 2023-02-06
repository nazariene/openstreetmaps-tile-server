#!/bin/bash

set -e
set -x

rm -rf /data/database || true
mkdir -p /data/database/postgres || true
tar --lzop -xvf /opt/postgres.tar.lzop -C /data/database

if [ -f "/opt/tiles.tar.lzop" ]; then
  rm -rf /data/tiles/ || true
  mkdir -p /data/tiles/default || true
  ln -s /data/tiles /var/cache/renderd/ || true
  tar --lzop -xvf /opt/tiles.tar.lzop -C /data/tiles
fi

