#! /usr/bin/env /usr/bin/python3

import mapnik

map = mapnik.Map(600,300)

map.background = mapnik.Color('steelblue')

polygons = mapnik.PolygonSymbolizer()
polygons.fill = mapnik.Color('lightgreen')

rules = mapnik.Rule() 
rules.symbols.append(polygons)

style = mapnik.Style() 
style.rules.append(rules) 
map.append_style('Countries', style)

layer = mapnik.Layer('world')
layer.datasource = mapnik.Shapefile(file='world-countries.shp')
layer.styles.append('Countries')
map.layers.append(layer)

map.zoom_all()

mapnik.render_to_file(map, 'poygon-plain.png', 'png')
