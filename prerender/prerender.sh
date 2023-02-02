#!/bin/sh

set -e
set -x

if [ ! -e "/prerender/prerender.${COUNTRY_CODE}.py" ]
then
  echo "Prerender file for ${COUNTRY_CODE} not found, skip prerendering"
  exit 0
fi
service postgresql start
#sudo chown renderer: /etc/renderd.conf
sudo -u renderer renderd -c /etc/renderd.conf

/prerender/prerender.${COUNTRY_CODE}.py

service postgresql stop
