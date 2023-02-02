FROM overv/openstreetmap-tile-server:2.2.0

ARG COUNTRY_CODE

COPY scripts/ scripts/

RUN chmod a+rwx /scripts/*

#Download map
RUN scripts/download_map.sh

#Translate
COPY translate/ translate/
RUN chmod a+rwx /translate/*
RUN translate/translate.sh

#Import map to postgres
RUN /run.sh import

#Prerender tiles to avoid on-demand rendering
COPY prerender/ prerender/
RUN chmod a+rwx /prerender/*
RUN prerender/prerender.sh

ENTRYPOINT ["/run.sh"]
CMD ["run"]
