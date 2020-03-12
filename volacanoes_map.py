import folium
import pandas 

# import the dataset as csv file
hv = pandas.read_csv("Holocene_Volcano.csv")
name_hv = list(hv["Volcano Name"])
elev_hv = list(hv["Elevation"])
lat_hv = list(hv["Latitude"])
lon_hv = list(hv["Longitude"])

pv = pandas.read_csv("Pleistocene_Volcano.csv")
name_pv = list(pv["Volcano Name"])
elev_pv = list(pv["Elevation"])
lat_pv = list(pv["Latitude"])
lon_pv = list(pv["Longitude"])

# stylize text
# put links in the popup window with the name of the volcano as a link 
# which does a Goggle search for that particulart volcano when clicked
html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Function to change the marker color  
# according to the elevation of volcano
def color(el):
    if el >= 3000: 
        return 'red'
    elif el >= 2000: 
        return 'orange'
    elif el >= 1000:
        return 'yellow'
    elif el >= 0: 
        return 'green'
    else:
        return 'blue'

# latitude -90 to 90 longitude -180 to 180
# Map object which center is Dallas-Fort worth Metropolitan Area 
# add zoom and tile parameter
map = folium.Map(location = [32.779951, -96.818092], zoom_start= 4, tiles = "Stamen Terrain")

# create a feature group 
fgh = folium.FeatureGroup(name = "Holocene Volcanoes")

# add multiple markers
for lt, ln, el, name in zip(lat_hv, lon_hv, elev_hv, name_hv):
    iframe = folium.IFrame(html=html % (name, name, el), width=180, height=80)
    fgh.add_child(folium.CircleMarker(location=[lt, ln], radius = 5, popup = folium.Popup(iframe), 
    fill_color = color(el), fill=True, color = 'none', fill_opacity = 0.8))

fgp = folium.FeatureGroup(name = "Pleistocene Volcanoes")

# add multiple markers
for lt, ln, el, name in zip(lat_pv, lon_pv, elev_pv, name_pv):
    iframe = folium.IFrame(html=html % (name, name, el), width=180, height=80)
    fgp.add_child(folium.CircleMarker(location=[lt, ln], num_sides = 3, radius = 5, popup = folium.Popup(iframe), 
    fill_color = color(el), fill=True, color = 'none', fill_opacity = 0.8))

map.add_child(fgh)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# save the HTML file created above
map.save("Volcanoes_Map.html")

