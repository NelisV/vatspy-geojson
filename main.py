import csv
import json

airspace_count = 0
fir_list = []
firpoint_list = None
firheader_list = None
# file_name = 'source/FIRBoundaries_test.dat'
file_name = 'source/FIRBoundaries.dat'



def fir_header(header):
    global airspace_count, firheader_list
    airspace_count += 1
    firheader_list = header


def airspace_pnt(firpoint_list, point):
    coords = [float(point[0]), float(point[1])]
    coords.reverse()
    point = [coords]
    if firpoint_list == None:
        firpoint_list = point
    else:
        firpoint_list = firpoint_list + point
    return firpoint_list


def airspace_close():
    global firheader_list, firpoint_list
    header = firheader_list + [firpoint_list]
    keys = ['ICAO', 'IsOceanic', 'IsExtension', 'PointCount', 'MinLat', 'MinLon', 'MaxLat', 'MaxLon', 'CenterLat', 'CenterLon', 'Coordinates']
    fir_dict = dict(zip(keys, header))
    firpoint_list = None
    return fir_dict


def geojson_writer(features):
    '''Create GeoJSON Header'''

    basedict = {}
    crsdict = {}
    propertydict = {}
    feature_list = []
    basedict['type'] = "FeatureCollection"
    basedict['name'] = ''
    propertydict['name'] = "urn:ogc:def:crs:OGC:1.3:CRS84"
    crsdict['type'] = "name"
    crsdict['properties'] = propertydict
    basedict['crs'] = crsdict
    for section in features:
        feature_list = feature_list + section[1]

    basedict['features'] = feature_list

    '''write to text file'''
    name = section[2]
    outputfile = open('output/{}.geojson'.format(name), 'w')
    outputfile.write(json.dumps(basedict, indent=4))
    # print(json.dumps(basedict, indent=4))
    outputfile.close()
    print_string = 'GeoJSON saved to {}.geojson'.format(name)
    print(print_string)


if __name__ == "__main__":
    with open(file_name) as fir_file:
        csv_reader = csv.reader(fir_file, delimiter='|')
        for row in csv_reader:
            if len(row) > 2:
                if airspace_count > 0:
                    fir_list.append(airspace_close())
                fir_header(row)
            else:
                firpoint_list = airspace_pnt(firpoint_list, row)
        fir_list.append(airspace_close())

    features = []
    airspace_count = 0
    for item in fir_list:
        airspace_count += 1
        filename = 'firboundaries'
        section = [12582, [
            {'type': 'Feature', 'properties': {'id': airspace_count, 'ICAO': item['ICAO'], 'IsOceanic': item['IsOceanic'], 'IsExtension': item['IsExtension'], 'PointCount': item['PointCount'], 'MinLat': item['MinLat'], 'MinLon': item['MinLon'], 'MaxLat': item['MaxLat'], 'MaxLon': item['MaxLon'], 'CenterLat': item['CenterLat'], 'CenterLon': item['CenterLon']}, 'geometry': {'type': 'MultiPolygon', 'coordinates': [[item['Coordinates']]]}}], filename]
        features.append(section)

    geojson_writer(features)