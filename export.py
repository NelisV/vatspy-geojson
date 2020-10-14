import json

with open('output/firboundaries.geojson') as json_file:
    data = json.load(json_file)
    f = open('export/FIRBoundaries.dat', 'w')
    for item in data['features']:
        coordinates = item['geometry']['coordinates'][0][0]
        feature = item['properties']
        headerline ='{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(feature['ICAO'], feature['IsOceanic'], feature['IsExtension'], len(coordinates), feature['MinLat'], feature['MinLon'], feature['MaxLat'], feature['MaxLon'], feature['CenterLat'], feature['CenterLon'])
        print(headerline)
        print(feature['PointCount'])
        f.write(headerline)
        for coord in coordinates:
            coordline = '{}|{}\n'.format(coord[1], coord[0])
            print(coordline)
            f.write(coordline)
    f.close()