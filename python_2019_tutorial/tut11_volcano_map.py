import folium
import pandas as pd
import sys


data = pd.read_csv("volcanoes_usa.txt")

# print(data)

lon = list(data['LON'])
lat = list(data['LAT'])
elev = list(data['ELEV'])
# print(lat)

# sys.exit()

def color_elev(eleva):
    if (eleva<1000):
        return 'green'
    elif (1000<=eleva<=3000):
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[46.856211, -112.366048],zoom_start=6, tiles='Mapbox bright')

fg = folium.FeatureGroup(name='Volcanoes')

for lt,ln,el in zip(lat,lon,elev):
    # print(el,color_elev(el))
    fg.add_child(folium.Marker(location=[lt, ln],popup=str(el)+' m',icon=folium.Icon(color=color_elev(el))))

map.add_child(fg)
# map.add_child(folium.LayerControl()) # to control the size of the marker

map.save('folium.html')