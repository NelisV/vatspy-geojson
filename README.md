# vatspy-geojson
To convert firboundaries.dat to GeoJSON:
1. Create a subfolder in the root directory called /source/.
2. Paste firboundaries.dat in the created folder.
3. Run main.py.

firboundaries.geojson is created in /output/


- When editing in QGIS, it is advised to first convert to ESRI Shapefile.
- Copy the sectors you want to edit to a new layer (important).
- Make you changes.
- When finished save your layer to GeoJSON.

To convert GeoJSON to firboundaries.dat:
1. Paste firboundaries.geojson you created in /output/
2. Run export.py
3. enter filename for input file (default is firboundaries.geojson)
3. firboundaries.dat created in /export/

- Make sure to only upload the sectors you edited.