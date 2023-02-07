#!/bin/bash

set -e
set -x

#Cleanup pg_wal
su - postgres -c '/usr/lib/postgresql/14/bin/pg_resetwal /var/lib/postgresql/14/main/'

#Archive postgres
cd /data/database
tar --lzop -cf /opt/postgres.tar.lzop postgres
rm -rf /data/database

#Archive rendered tiles
if [ -d "/data/tiles/default" ]; then
  cd /data/tiles
  tar --lzop -cf /opt/tiles.tar.lzop default
  rm -rf /data/tiles
fi
