import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

latitudes = []
longitudes = []
for row in c.execute('SELECT * FROM locations_coordinates WHERE account_id is 4'):
    latitudes.append(row[1])
    longitudes.append(row[2])

import gmplot
gmap = gmplot.GoogleMapPlotter(40.732918, -73.992582, 16)

# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
gmap.scatter(latitudes, longitudes, '#3B0B39', size=10, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")