#! /usr/bin/env /usr/bin/python3

import mapnik

map = mapnik.Map(600,300)

mapnik.load_map(map, 'point.xml')

map.zoom_all()
map.zoom(-1.1)

mapnik.render_to_file(map, 'point.png', 'png')

