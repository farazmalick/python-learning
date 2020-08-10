import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")


fgv = folium.FeatureGroup(name="Volcanoes")
# for cordinates in [[38.2, -99.1], [39.2, -97.1]]:
#     fg.add_child(folium.Marker(
#         location=cordinates, popup="Marker", icon=folium.Icon(color='green')))


def elevation_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# for lt, lo, el in zip(lat, lon, elev):
#     fg.add_child(folium.Marker(
#         location=[lt, lo], popup=str(el)+" m", icon=folium.Icon(color=elevation_color(el))))
for lt, lo, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, lo], radius=6, popup=str(el)+" m", fill_color=elevation_color(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(open("world.json", encoding="utf-8-sig").read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                                                                        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
