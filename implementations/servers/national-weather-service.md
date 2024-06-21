# US National Weather Service EDR-API Server Implementation

The NWS implementation of the EDR-API was originally forked from pygeoapi and customized code was developed to prototype the NWS's use cases.
The implementation supports position, area, cube, trajectory, and corridor queries as well as items and locations. The implementation provides 
schema support for CoverageJSON, JSON, text, XML in the form of IWXXM, GRIB, NetCDF, and Cloud Optimized Geotiff.
This implementation uses a variety of open source software such as Flask, Gunicorn, Xarray, Dask, and Zarr to name a few.


## Demo deployment

- Landing page:  https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype *This site should be publicly available.*
- OpenAPI document (Swagger):  https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype/api?f=html *This site should be publicly available.*


Sample requests:
- Position query (supports CoverageJSON):
  - https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_lv_ISBL0_Isobaric_surface_Pa/instances/00z/position?coords=POINT(-77.157279 38.78349)&parameter-name=TMP_P0_L100_GLL0&datetime=2021-05-18T00:00:00/2021-05-18T15:00:00&Z=97500.0/100000.0&crs=EPSG:4326&interpolation=nearest_neighbor&f=CoverageJSON

- Area query (supports CoverageJSON, GRIB, NetCDF, COGeotiff):
  - https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_lv_ISBL0_Isobaric_surface_Pa/instances/00z/area?coords=POLYGON((-126.061604 54.20588,-130.562503 33.085059,-75.707833 15.768079,-52.359439 55.180992,-126.061604 54.20588))&parameter-name=TMP_P0_L100_GLL0&datetime=2021-05-18T00:00:00/2021-05-18T12:00:00&Z=97500.0/100000.0&crs=EPSG:4326&interpolation-x=nearest_neighbor&interpolation-y=nearest_neighbor&f=CoverageJSON

- Cube query (supports CoverageJSON, GRIB, NetCDF, COGeotiff):
  - https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_lv_ISBL0_Isobaric_surface_Pa/instances/00z/cube?coords=POLYGON((-125.715082 30.103966,-125.715082 51.070047,-65.374949 51.070047,-65.374949 30.103966,-125.715082 30.103966))&parameter-name=TMP_P0_L100_GLL0&datetime=2021-05-18T00:00:00/2021-05-18T18:00:00&Z=95000.0/100000.0&crs=EPSG:4326&interpolation-x=nearest_neighbor&interpolation-y=nearest_neighbor&f=CoverageJSON

- Trajectory query (supports CoverageJSON, NetCDF):
  - https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_lv_ISBL0_Isobaric_surface_Pa/instances/00z/trajectory?coords=LINESTRINGZM(-125.29312321978699 34.91839251355151 95000.0 2021-05-22T03:00:00,-109.39933481554934 45.95296306707622 97500.0 2021-05-27T06:00:00,-84.57407951893437 34.33990519783608 92500.0 2021-05-31T12:00:00,-69.66486447564097 46.536403051349836 100000.0 2021-06-02T15:00:00)&parameter-name=TMP_P0_L100_GLL0&crs=EPSG:4326&f=CoverageJSON

- Corridor query (supports CoverageJSON):
  - https://edr-api-c.mdl.nws.noaa.gov/OGC-API-Prototype/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_lv_ISBL0_Isobaric_surface_Pa/instances/00z/corridor?coords=LINESTRING(-129.44238756731704 35.607235703724754,-112.07174113372025 47.77925662583127,-90.27053000164618 33.640421980932636,-72.19661726490963 37.74954997476914)&parameter-name=TMP_P0_L100_GLL0&datetime=2021-05-18T00:00:00&Z=1.0&crs=EPSG:4326&resolution-x=100&corridor-width=100&f=CoverageJSON 


