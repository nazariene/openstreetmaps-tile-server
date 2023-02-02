#!/bin/bash

set -e
set -x

if [ ! -e "/translate/${COUNTRY_CODE}_translation.xml" ]
then
  echo "Translate file for ${COUNTRY_CODE} not found, skip translation"
  exit 0
fi

osmosis --read-pbf file="/data/region.osm.pbf" --tag-transform file="/translate/${COUNTRY_CODE}_translation.xml"  --write-pbf file="/data/translated.osm.pbf"
rm -rf /data/region.osm.pbf
mv /data/translated.osm.pbf /data/region.osm.pbf
