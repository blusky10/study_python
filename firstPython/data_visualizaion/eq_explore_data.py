import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename='d:\\STUDY\\study_python\\firstPython\\data_visualizaion\\data\\eq_data_1_day_m1.json'
readable_file='d:\\STUDY\\study_python\\firstPython\\data_visualizaion\\data\\eq_data_1_day_m1_readable.json'

# with open(filename) as f:
#     all_eq_data = json.load(f)

# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

with open(readable_file) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats=[], [], []
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

data=[
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker':{
            'size':[5*mag for mag in mags]
        }
    }
]
my_layout=Layout(title='global earthquakes')

fig={'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')