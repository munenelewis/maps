import folium


map = folium.Map(location=[-1.285803,36.698874], zoom_start=8, tiles='Mapbox Bright')

map.add_child(folium.Marker(location=[-1.285803,36.698874], popup ="hi am a marker", icon=folium.Icon(color='red')))


map.save('map1.html')

