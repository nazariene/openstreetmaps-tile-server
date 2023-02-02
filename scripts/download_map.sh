#!/bin/bash

set -e
set -x

case $COUNTRY_CODE in
"by") COUNTRY_URN="europe/belarus-latest.osm.pbf";;
"kz") COUNTRY_URN="asia/kazakhstan-latest.osm.pbf";;
"cn") COUNTRY_URN="asia/china-latest.osm.pbf";;
"ru") COUNTRY_URN="russia-latest.osm.pbf";;
"az") COUNTRY_URN="asia/azerbaijan-latest.osm.pbf";;
"ir") COUNTRY_URN="asia/iran-latest.osm.pbf";;
"mn") COUNTRY_URN="asia/mongolia-latest.osm.pbf";;
"eg") COUNTRY_URN="africa/egypt-latest.osm.pbf";;
esac

wget http://download.geofabrik.de/${COUNTRY_URN} -O /data/region.osm.pbf
