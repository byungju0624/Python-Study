import folium as foli
map = foli.Map(location=[37.5168606208383, 127.11127481121775], zoom_start=17)
map.save("./map.html")