import folium
import pandas

data= pandas.read_csv('Volcanoes.txt')

lon = list(data['LON'])
lat = list(data['LAT'])
elev = list(data['ELEV'])

def color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=8, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="My Map")



for lt , ln , el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup =str(el) + 'meters', icon=folium.Icon(color=color(el))))

map.add_child(fg)

map.save('map1.html')

