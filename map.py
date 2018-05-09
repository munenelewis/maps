import folium
import pandas

data= pandas.read_csv('Volcanoes.txt')

lon = list(data['LON'])
lat = list(data['LAT'])


map = folium.Map(location=[-1.285803,36.698874], zoom_start=8, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="My Map")



for lt , ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup ="hi am a marker", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save('map1.html')

