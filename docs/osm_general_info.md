---
OpenStreetMaps General Info
---

# Components
## OSM
OSM is a webserver that serves map tiles (png images)

## Nominatim
Nominatim uses OpenStreetMap data to find locations on Earth by name and address (geocoding). It can also do the reverse, find an address for any location on the planet.


# OSM files
An OSM file is **a street map saved in the OpenStreetMap (OSM) format**. It contains XML-formatted data in the form of "nodes" (points), "ways" (connections), and "relations" (street and object properties, such as **tags**).

OSM file can have following formats:
- .osm - plain osm xml data
- .osm.bz2 - gzipped osm xml data
- .osm.pbf - protobuf osm data, alternative to xml

OSM file can be opened and edited via many tools (https://wiki.openstreetmap.org/wiki/Editors).
Personal recommendation: use JOSM (https://wiki.openstreetmap.org/wiki/JOSM).

## Tags
Objects in OSM data may have many names - but only some of them will be shown on rendered tiles.
For example, Tokyo might have multiple names (in english, in japanese, in hebrew, etc), but only english name will be rendered (or japanese, doesn't matter).
Each name is contained inside **tag**, e.g.:
- name:en -> Tokyo
- name:japanese -> _東京都_
- name -> Tokyo

**name** without an extension (:country_code) is considered to be **default** name and used for rendering most of the time (unless specific rendering rules are set).

# Rendering OSM files
## Loading OSM files into DB
OSM files are loaded into Postgres using osm2pgsql tool (https://osm2pgsql.org/). Osm2pgsql imports OSM data into a PostgreSQL/PostGIS database. It is an essential part of many rendering toolchains, the Nominatim geocoder and other applications processing OSM data.

## Rendering DB data
After data is loaded into DB, rendering engine is used to render raster tiles (images) from loaded data. Usually, Mapnik (https://mapnik.org/) is used as a renderer engine and openstreetmap-carto (https://wiki.openstreetmap.org/wiki/OpenStreetMap_Carto) is used as a stylesheet for rendering (i.e. used to customize the output).

## Serving raster images to browser
After rendering is done, raster tiles are server by nginx to the client.

Tiles are either rendered on-demand or can be predendered.
Tile rendering can be **very** time consuming process, so predendering is advised.


# Modifying OSM files
You can modify map before rendering tiles in multiple ways:
- Modify source .osm file before loading into DB (see [[Transforming OSM data using Osmosis]])
- Modify DB contents after data has been loaded, but before rendering tiles (see [[Transforming OSM data using OpenStreetMaps-carto and osm2pgsql]])
- Manually update DB after OSM data was loaded, but before rendering

## Modifying default language
Objects in OSM data may have many names - but only some of them will be shown on rendered tiles.
For example, Tokyo might have multiple names (in english, in japanese, in hebrew, etc), but only english name will be rendered (or japanese, doesn't matter).
Each name is contained inside **tag**, e.g.:
- name:en -> Tokyo
- name:japanese -> _東京都_
- name -> Tokyo

**name** without an extension (:country_code) is considered to be **default** name and used for rendering most of the time (unless specific rendering rules are set).

## Modifying max zoom-level
Max zoom level is controlled in 3 places:
- Max zoom level that raster images can rendered for
- Max zoom for which on-demand rendering is available
- Max zoom level that built-in web ui will allow

Rendering zoom level is controlled in osm-carto stylesheet - project.mml. You're looking for top-level property called "maxzoom". Default value is 18. Setting this to higher level will allow osm-carto to render more detailed raster images.

On-demand rendering is controlled by mod_tile (nginx plugin) settings. See renderd.conf file, setting "MAXZOOM". **Max value here is 20**. Setting this above 20 is NOT possible due to mod_tile limitations (the way it stores data). It's possible to recompile mod_tile with modifications to overcome this limitations - see [here](https://github.com/SomeoneElseOSM/mod_tile/commit/d4db05fef67eedebbbaf39e00f30e11fa84d4d79)

Web server's zoom level (i.e. maximum zoom level that is allowed for web-ui to zoom into) is controller by LeafLet webapp's settings. Generally you're using your own app, so either skip configuring this or just makes changes in browser runtime.