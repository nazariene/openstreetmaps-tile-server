FROM overv/openstreetmap-tile-server:2.2.0

ARG COUNTRY_CODE

RUN apt-get update && apt-get install -y lzop

#Download map
COPY scripts/download_map.sh scripts/download_map.sh
RUN chmod a+rwx /scripts/download_map.sh
RUN scripts/download_map.sh

#Translate map
COPY translate/ translate/
RUN chmod a+rwx /translate/*
RUN translate/translate.sh

#Set custom style - in order to remove ocean water polygons - they eat a LOT of space
COPY style/external-data.yml /home/renderer/src/openstreetmap-carto-backup/external-data.yml
COPY style/project.mml /home/renderer/src/openstreetmap-carto-backup/project.mml

#Import map to postgres
RUN OSM2PGSQL_EXTRA_ARGS="--drop" /run.sh import

#Prerender tiles to avoid on-demand rendering
COPY prerender/ prerender/
RUN chmod a+rwx /prerender/*
RUN prerender/prerender.sh

#Cleanup
COPY scripts/cleanup.sh scripts/cleanup.sh
RUN chmod a+rwx /scripts/cleanup.sh
RUN scripts/cleanup.sh

#Archive rendered tiles and postgres data to reduce image size
COPY scripts/compact_data.sh scripts/compact_data.sh
RUN chmod a+rwx /scripts/compact_data.sh
RUN scripts/compact_data.sh
COPY scripts/unpack_data.sh scripts/unpack_data.sh
RUN chmod a+rwx /scripts/unpack_data.sh

#Copy run script
COPY scripts/run.sh scripts/run.sh
RUN chmod a+rwx /scripts/run.sh

ENTRYPOINT ["/scripts/run.sh"]
