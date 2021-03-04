import json

infile = open("US_fires_9_1.json",'r')


fire_data = json.load(infile)  # convert to python object which can be used in python.



lons,lats,brights = [],[],[]

for fire in fire_data:
    lon = fire["longitude"]
    lat = fire["latitude"]
    bright = fire["brightness"]
    if bright > 450:
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)
    


print(lons[:10])
print(lats[:10])  # show the first 10
print(brights[:10])



from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
            'size':[.04* bright for bright in brights],
            'color':brights,
            'colorscale':'Viridis',
            'reversescale':True,
            'colorbar':{"title":"Brightness"}}
    }
]



my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_Fires_9_1.html")



