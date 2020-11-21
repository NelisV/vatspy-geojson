# vatspy-geojson
To convert Firboundaries to GEOJson:
1. create a subfolder in the root directory called /source/.
2. paste your firboundaries.dat in the created folder.
3. run main.py.
firboundaries.geojson is created in /output/

- When editing in QGIS, it is advised to first convert to ESRI Shapefile
- when finished save your layer to GEOJSON

To convert GEOJson to Firboundaries:
1. Paste firboundaries.geojson you created in /output/
2. Run export.py
3. valid Firboundaries.dat created in /export/

- when uploading to github, only upload the sectors you edited, not the entire file created by the script. 