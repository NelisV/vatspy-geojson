import json


def dat_export(file_name, output_dir):
    print('file_name {}'.format(file_name))
    print('output_dir {}'.format(output_dir))
    with open(file_name) as json_file:
        data = json.load(json_file)
        f = open(output_dir, 'w')
        for item in data['features']:
            coordinates = item['geometry']['coordinates'][0][0]
            feature = item['properties']
            if 'IsExtensio' in feature:
                header_line = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(feature['ICAO'], feature['IsOceanic'],
                                                                       feature['IsExtensio'], len(coordinates),
                                                                       round(float(feature['MinLat']), 6),
                                                                       round(float(feature['MinLon']), 6),
                                                                       round(float(feature['MaxLat']), 6),
                                                                       round(float(feature['MaxLon']), 6),
                                                                       round(float(feature['CenterLat']), 6),
                                                                       round(float(feature['CenterLon']), 6))
            elif 'IsExtension' in feature:
                header_line = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(feature['ICAO'], feature['IsOceanic'],
                                                                       feature['IsExtension'], len(coordinates),
                                                                       round(float(feature['MinLat']), 6),
                                                                       round(float(feature['MinLon']), 6),
                                                                       round(float(feature['MaxLat']), 6),
                                                                       round(float(feature['MaxLon']), 6),
                                                                       round(float(feature['CenterLat']), 6),
                                                                       round(float(feature['CenterLon']), 6))
            f.write(header_line)
            for coord in coordinates:
                val1 = round(coord[1], 6)
                val2 = round(coord[0], 6)
                coord_line = '{}|{}\n'.format(val1, val2)
                f.write(coord_line)
        f.close()


if __name__ == "__main__":
    dat_export('F:/Documents/Dutchvacc/SCT werk/VATSPY/PR.328/328.geojson',
               'F:/Documents/Dutchvacc/SCT werk/VATSPY/PR.328/328test.dat')
