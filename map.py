import folium


map = folium.Map(location=[-1.285803,36.698874], zoom_start=8, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="My Map")

for coodinates in [[-1.285803,36.698874],[-2.285803,36.698874],[-3.285803,36.698874]]:
    fg.add_child(folium.Marker(location=coodinates, popup ="hi am a marker", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save('map1.html')

