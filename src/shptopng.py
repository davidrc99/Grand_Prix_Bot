import mapnik
import collections.abc

m = mapnik.Map(1000,1000) # 1000x1000
m.background = mapnik.Color('steelblue') #Fondo de color azul clarito guapo

###########
s = mapnik.Style() # style object to hold rules
r = mapnik.Rule() # rule object to hold symbolizers
# to fill a polygon we create a PolygonSymbolizer
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) # add the symbolizer to the rule object

# to add outlines to a polygon we create a LineSymbolizer
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer) # add the symbolizer to the rule object
s.rules.append(r) # now add the rule to the style and we're done
#########
m.append_style('My Style',s) # Styles are given names only as they are applied to the map
#########
ds = mapnik.Shapefile(file='./data/data.shp')

layer = mapnik.Layer('world') # new layer called 'world' (we could name it anything)
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
# Write the data to a png image called world.png in the current directory
mapnik.render_to_file(m,'./img/prueba.png', 'png')

# Exit the Python interpreter
exit() # or ctrl-d
