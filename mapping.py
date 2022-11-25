import folium
import pandas as pd

data = pd.read_json('fav_restaurants.json')

#Extracting single lists from the data frame
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
price = list(data['PRICE RANGE'])
link = list(data['URL'])
street = list(data['STREET'])
cat = list(data['CATEGORY'])

#Defining the marker colors based on the price range
def marker_color(pricerange):
    if pricerange == '$':
        return 'lightgreen'
    elif pricerange == '$$':
        return 'green'
    elif pricerange == '$$$':
        return 'darkgreen'        

#Creating an html object to define the structure of the marker text
html = """<b>%s</b><br>
%s<br>
<a href="%s">%s</a><br><br>
What you can expect:<br>
%s<br><br>
Price Range:<br>
%s<br>
"""

#Creating the base map
map = folium.Map(location=[52.51, 13.40], zoom_start=12, tiles = "Stamen Terrain")

#Creating a feature group to add multiple markers
fg = folium.FeatureGroup(name='My Favorite Restaurants in Berlin')

#Loop through the file to add all markers
for lt, ln, n, l, p, s, c in zip(lat, lon, name, link, price, street, cat):
    iframe = folium.IFrame(html=html%(n, s, l, l, c, p), width=300, height=200)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(icon='leaf', color=marker_color(p))))

map.add_child(fg)
map.save('FavesInBerlin.html')

