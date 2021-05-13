import json

vertexcnt = 0

print('Enter filename.. (GeoJSON)')
filename = input()
path = 'output/{}'.format(filename)

with open(path) as json_file:
    data = json.load(json_file)
    f = open('export/FIRBoundaries.dat', 'w')
    for item in data['features']:
        coordinates = item['geometry']['coordinates'][0][0]
        feature = item['properties']
        headerline = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(feature['ICAO'], feature['IsOceanic'], feature['IsExtensio'], len(coordinates), round(float(feature['MinLat']), 6), round(float(feature['MinLon']), 6), round(float(feature['MaxLat']), 6), round(float(feature['MaxLon']), 6), round(float(feature['CenterLat']), 6), round(float(feature['CenterLon']), 6))
        print(headerline)
        print(feature['PointCount'])

        # if vertexcnt < len(coordinates):
        #
        # vertexcnt = len(coordinates)

        f.write(headerline)
        for coord in coordinates:
            val1 = round(coord[1], 6)
            val2 = round(coord[0], 6)
            # coordline = '{}|{}\n'.format(coord[1], coord[0])
            coordline = '{}|{}\n'.format(val1, val2)
            print(coordline)
            f.write(coordline)
    f.close()