# OpenStreetMap (OSM) tile-server

Used to provide map tiles (raster images, png) for UI when public tile-servers can't be reached.

Uses community tile-server (overv/openstreetmap-tile-server) with modifications:

- Allows to download map by country code
- Applies tag-transformation per country
- Prependers tiles per country


## Add new country map
- Edit scripts/download_map.sh file - add country code and country urn to download map

## Customize map - translate names
- Add ${COUNTRY_CODE}_translation.xml to "translate" folder
- Use https://wiki.openstreetmap.org/wiki/Osmosis/TagTransform#output to understand the syntax

## Prerender country tiles
- Add prerender.${COUNTRY_CODE}.py to "prerender" folder
- Fill up coordinates and zoomlevels to prerender

Prerendering might take a VERY long time and eat-up all your CPU and RAM. Stay frosty.


# Docs
[General Info](https://github.com/nazariene/openstreetmaps-tile-server/blob/master/docs/osm_general_info.md)

[Transform map before loading to postgresql](https://github.com/nazariene/openstreetmaps-tile-server/blob/master/docs/transform_osm_data_osmosis.md)

[Transform map during loading to postgresql](https://github.com/nazariene/openstreetmaps-tile-server/blob/master/docs/transform_osm_data_carto.md)