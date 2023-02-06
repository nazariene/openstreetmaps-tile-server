#!/bin/bash

set -e
set -x

apt-get -qq purge osmosis osm2pgsql
apt-get clean

#Delete downloaded map
rm -rf /data/region.osm.pbf


rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

