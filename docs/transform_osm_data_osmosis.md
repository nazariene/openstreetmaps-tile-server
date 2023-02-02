---
Transforming OSM data using Osmosis
---

OSM data (.osm, .osm.bz2, .osm.pbf) can be transformed before loading into DB.

[Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis) is a command line Java application for processing OSM data. The tool consists of pluggable components that can be chained to perform a larger operation.

### Tags
Objects in OSM data may have many names - but only some of them will be shown on rendered tiles.
For example, Tokyo might have multiple names (in english, in japanese, in hebrew, etc), but only english name will be rendered (or japanese, doesn't matter).
Each name is contained inside **tag**, e.g.:
- name:en -> Tokyo
- name:japanese -> _東京都_
- name -> Tokyo

**name** without an extension (:country_code) is considered to be **default** name and used for rendering most of the time (unless specific rendering rules are set).

### Tag-Transform
To change names [**tag-transform** plugin](https://wiki.openstreetmap.org/wiki/Osmosis/TagTransform) of Osmosis can be used.
It requires input file and transformation xml.
Following transformation XML searches "name:en" tag in objects and, if found, sets value from that tag to "name" - effectively telling to use English names as default name **if** they are present. Objects without english names will be left untouched.
```xml
<?xml version="1.0"?>
<translations>
    <translation>
        <name>Azerbaijan translation</name>
        <description>
            Set all "name" tag values to appropriate "name:az" value.
        </description>
        <match mode="or">
            <tag k="name:en" match_id="translation" v=".*"/>
        </match>
        <output>
            <copy-all/>
            <tag k="name" from_match="translation" v="{0}"/>
        </output>
    </translation>
</translations>
```

`./osmosis*/bin/osmosis --read-xml file=YOURFILE --tag-transform file=TRANSFORM.xml --write-xml file=OUTFILE`

To work with .pbf files use **--read-pbf** and **--write-pbf**