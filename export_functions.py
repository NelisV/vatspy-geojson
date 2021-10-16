import geojson
from geojson import Feature, MultiPolygon


def dat_export(file_name, output_dir):
    print('file_name {}'.format(file_name))
    print('output_dir {}'.format(output_dir))

    with open(file_name) as f:
        gj = geojson.load(f)
        split_id = []
        u_id = {}
        new_feature_list = []
        print(gj['name'])

        for feature in gj['features']:
            if feature['properties']['id'] not in u_id.keys():
                u_id[feature['properties']['id']] = feature['properties']['oceanic']
                feature['properties']['extension'] = '0'
            else:
                if u_id[feature['properties']['id']] == feature['properties']['oceanic']:
                    feature['properties']['extension'] = '1'
                else:
                    feature['properties']['extension'] = '0'
            # need to be split
            if len(feature['geometry']['coordinates']) > 1:
                extension = False
                for polygon in feature['geometry']['coordinates']:
                    if feature['properties']['id'] not in split_id:
                        extension = '0'
                        split_id.append(feature['properties']['id'])
                    else:
                        extension = '1'
                    polygon = MultiPolygon([[[tuple(x) for x in polygon[0]]]])
                    new_feature = Feature(geometry=polygon, properties={'id': feature['properties']['id'],
                                                                            'oceanic': feature['properties'][
                                                                                'oceanic'],
                                                                            'extension': extension,
                                                                            'label_lon': feature['properties'][
                                                                                'label_lon'],
                                                                            'label_lat': feature['properties'][
                                                                                'label_lat']
                                                                            })
                    new_feature_list.append(new_feature)

            else:
                # no need to be split
                new_feature_list.append(feature)

        gj['features'] = new_feature_list

        # start building output
        f = open(output_dir, 'w')
        for feature in gj['features']:
            coordinates = feature['geometry']['coordinates'][0][0]
            properties = feature['properties']

            point_count = len(coordinates)
            min_lat = min(coordinates, key=lambda x: x[1])[1]
            min_lon = min(coordinates, key=lambda x: x[0])[0]
            max_lat = max(coordinates, key=lambda x: x[1])[1]
            max_lon = max(coordinates, key=lambda x: x[0])[0]

            header_line = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(properties['id'], properties['oceanic'],
                                                                   properties['extension'], point_count,
                                                                   min_lat,
                                                                   min_lon,
                                                                   max_lat,
                                                                   max_lon,
                                                                   properties['label_lat'],
                                                                   properties['label_lon'])
            f.write(header_line)
            for coord in coordinates:
                val1 = round(coord[1], 6)
                val2 = round(coord[0], 6)
                coord_line = '{}|{}\n'.format(val1, val2)
                f.write(coord_line)
        f.close()


if __name__ == "__main__":
    dat_export(r'C:\Users\niels\PycharmProjects\vatspy-geojson\newdatafile_test\DAT\test\converted to gj\firboundaries.geojson',
               r'C:\Users\niels\PycharmProjects\vatspy-geojson\newdatafile_test\DAT\Firboundaries.dat')
