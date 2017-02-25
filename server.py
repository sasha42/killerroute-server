from flask import Flask, jsonify, request
import json

import pyproj
from shapely.geometry import Polygon, Point
from shapely.ops import transform
from functools import partial

app = Flask(__name__)

@app.route('/crime/api', methods=['POST'])
def find_points():
    # parse the posted data
    locs = []

    for point in request.json:
        lat = point['lat']
        lng = point['lng']

        locs.append([lat,lng])

    locs = tuple(locs)

    # create polygon
    poly = Polygon(locs)

    # create list of points for output
    points_in_polygons = []

    # test if points in list are in the database
    with open('data.json') as data_file:    
        just_loc = json.load(data_file)

    for location in just_loc:
        try:
            lat = float(location[0])
            lon = float(location[1])
        except: 
            pass
        loc_point = Point(lat,lon)
        
        if poly.contains(loc_point) == True:
            location = lat,lon
            points_in_polygons.append(location)

    return jsonify({'points': points_in_polygons}), 201

if __name__ == '__main__':
    project = partial(
        pyproj.transform,
        pyproj.Proj(init='epsg:4326'),
        pyproj.Proj('+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs'))
    
    app.run(debug=False, host="0.0.0.0")