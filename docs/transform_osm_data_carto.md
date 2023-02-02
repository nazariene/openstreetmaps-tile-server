---
Transforming OSM data using OpenStreetMaps-carto and osm2pgsql
---

OSM data can be transformed after loading to DB, but before rendering.

You can use osm-carto in conjuction with osm2pgsql to apply styling (transformations) to osm data.
[osm-carto](https://wiki.openstreetmap.org/wiki/OpenStreetMap_Carto/) is an open-source [stylesheet](https://wiki.openstreetmap.org/wiki/Stylesheets "Stylesheets") for [rendering](https://wiki.openstreetmap.org/wiki/Rendering "Rendering") OpenStreetMap data to raster tiles.

OpenStreetMap Carto uses the PostgreSQL [hstore](http://www.postgresqltutorial.com/postgresql-hstore/) (extension and data type) and is pre-processed with  [![Font Awesome 5 brands github.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/16px-Font_Awesome_5_brands_github.svg.png)](https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua) [a lua script](https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua) by the [osm2pgsql](https://wiki.openstreetmap.org/wiki/Osm2pgsql "Osm2pgsql") tool.

General project configuration is included in  [![Font Awesome 5 brands github.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/16px-Font_Awesome_5_brands_github.svg.png)](https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml) [project.mml](https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml) (YAML). There are defined so called "layers", which include mainly SQL statements selecting the objects, while actual styling is done in multiple MSS files.

Example of MSS file for styling countries - note the **text-name: "[name]"** field:
```json
.country {  
  [zoom >= 3] {  
    text-name: "[name]";  
    text-size: 10;  
    text-wrap-width: 35; // 3.5 em  
    text-line-spacing: -1.5; // -0.15 em  
    text-margin: 7.0; // 0.7 em  
    [zoom >= 4] {  
      text-size: 11;  
      text-wrap-width: 40; // 3.6 em  
      text-line-spacing: -1.4; // -0.13 em  
      text-margin: 7.7; // 0.7 em  
    }  
    [zoom >= 5] {  
      text-size: 12;  
      text-wrap-width: 45; // 3.8 em  
      text-line-spacing: -1.2; // -0.10 em  
      text-margin: 8.4; // 0.7 em  
    }  
    [zoom >= 7] {  
      text-size: 13;  
      text-wrap-width: 50; // 3.8 em  
      text-line-spacing: -1.0; // -0.08 em  
      text-margin: 9.1; // 0.7 em  
    }  
    [zoom >= 10] {  
      text-size: 14;  
      text-wrap-width: 55; // 3.9 em  
      text-line-spacing: -0.7; // -0.05 em  
    }  
    text-fill: @country-labels;  
    text-face-name: @book-fonts;  
    text-halo-fill: @standard-halo-fill;  
    text-halo-radius: @standard-halo-radius * 1.5;  
    text-placement: interior;  
    text-character-spacing: 0.5;  
  }  
}
```

To apply modifications with styling you have to change osm-carto mml and mss files.