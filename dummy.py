import mapnik

map = mapnik.Map(600,300)

mapnik.render_to_file(map, 'dummy.png', 'png')
