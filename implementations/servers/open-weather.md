# Open Weather

[Open Weather](https://www.iblsoft.com/products/open-weather) is a general-purpose weather data processing software. It is able to ingest raw meteorological data in numerous data formats, organize the data in a database and then expose the data via various interfaces including

- Command-line interface (shell)
- Python API
- Web services, such as WCS and OGC-API EDR

Open Weather's EDR implementation supports gridded data (NWP, radar, sattelite) as well as point data (in-situ observations).

When deployed in cloud, Open Weather can process data on a very large scale with low latency.

## Demo Server

- Landing page: [https://ogcie.iblsoft.com/edr](https://ogcie.iblsoft.com/edr)
- OpenAPI schema: [https://ogcie.iblsoft.com/edr/api?f=JSON](https://ogcie.iblsoft.com/edr/api?f=JSON)

## Sample requests
***Note: The demo server contains live data not older than two days. Therefore, before you execute the queries below, please update 'datetime' URL parameter to the present date.***

### Position
#### Single Point
GFS 850 hPa temperature in Bratislava at 2021-01-19 09:00:00 UTC:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/position?parameter-name=temperature&datetime=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON`

#### Vertical Profile
GFS temperature in Bratislava at 2021-01-19 09:00 UTC, all available vertical levels:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/position?parameter-name=temperature&datetime=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=../..&f=CoverageJSON`

#### Time Series
GFS 850 hPa temperature in Bratislava from 2021-01-19 00:00 UTC until 2021-01-20 00:00 UTC @ 1h step:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/position?parameter-name=temperature&datetime=R25/2021-01-19T00:00:00/PT1H&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON`

### Radius
Air temperature, wind speed and wind direction from METARs within 100 km radius around Bratislava, 24h interval:

`https://ogcie.iblsoft.com/edr/collections/metar/radius?parameter-name=station,validity,air-temperature,wind-speed,wind-direction&coords=POINT(17.21 48.18)&within=100&within-units=km&datetime=2021-01-19T00:00:00/2021-01-20T00:00:00&f=KernelTSV`

### Area
#### Single Time and Level - Native Resolution
GFS wind (U and V component) within Slovakia at 2020-01-19 06:00 UTC, 850 hPa:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/area?parameter-name=u-component-of-wind,v-component-of-wind&datetime=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2`

#### Single Time and Level - Oversampled
The same as above but with higher spatial resolution:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/area?parameter-name=u-component-of-wind,v-component-of-wind&datetime=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&resolution-x=100&resolution-y=50&z=850&f=GRIB2`

#### Extruded in Vertical Dimension (Vertical Profile)
Wind (U and V component) within Slovakia at 2021-01-19 06:00 UTC, all vertical layers up to 300 hPa:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/area?parameter-name=u-component-of-wind,v-component-of-wind&datetime=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=../300&f=GRIB2`

#### Extruded in Time Dimension (Time Series)
Wind (U and V component) within Slovakia, all available forecasts starting from 2021-01-19 06:00 UTC, 850 hPa:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/area?parameter-name=u-component-of-wind,v-component-of-wind&datetime=2021-01-19T06:00:00/..&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2`

### Cube
#### GFS Data Within 4D Cube - Native Resolution
- Model: GFS
- Parameter: Air Temperature
- Bounding Box: 16.82 - 22.57E; 47.73 - 49.62N
- Vertical Extent: 1000 hPa → 300 hPa
- Time Extent: 2021-01-19 06:00 UTC → 2021-01-20 06:00 UTC
- Output format: GRIB2

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/cube?parameter-name=temperature&bbox=16.82,47.73,22.57,49.62&z=1000/300&datetime=2021-01-19T06:00:00/2021-01-20T06:00:00&f=GRIB2`

#### GFS Data Within 4D Cube - Oversampled
The same as above but with a denser sampling (in all dimensions):

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/cube?parameter-name=temperature&bbox=16.82,47.73,22.57,49.62&resolution-x=24&resolution-y=8&z=R14/1000/-50&&datetime=R25/2021-01-19T06:00:00/PT1H&f=GRIB2`

#### TEMP Within 4D Cube
- Parameters: Pressure, Geopotential Height, Air Temperature, Wind- Speed, Wind Direction
- Bounding Box: 16.82 - 22.57E; 47.73 - 49.62N
- Vertical Extent: 1000 hPa → 300 hPa
- Time Extent: 2021-01-18 06:00 UTC → 2021-01-20 06:00 UTC

`https://ogcie.iblsoft.com/edr/collections/temp-pressure/cube?parameter-name=station,validity,pressure,geopotential,air-temperature,wind-speed,wind-direction&bbox=16.82,47.73,22.57,49.62&z=1000/300&datetime=2021-01-18T06:00:00/2021-01-20T06:00:00&f=KernelTSV`

### Trajectory
#### XY Trajectory (LINESTRING)
Fixed time and vertical coordinate, 100 samples along trajectory:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/trajectory?parameter-name=temperature&datetime=2021-01-19T06:00:00&coords=LINESTRING(14.74 43.44, 9.39 46.89, 14.42 48.05, 7.66 51.4, 7.1 55.9, 2.31 53.72)&resolution=100&z=850&f=CoverageJSON`

Tip: Add vertical interval to form a "curtain": `z=1000/300`

#### XYZ Trajectory (LINESTRINGZ)
Fixed time coordinate, 100 samples along trajectory:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/trajectory?parameter-name=temperature&datetime=2021-01-19T06:00:00&coords=LINESTRINGZ(14.74 43.44 1000, 9.39 46.89 800, 14.42 48.05 500, 7.66 51.4 500, 7.1 55.9 700, 2.31 53.72 1000)&resolution=100&f=CoverageJSON`

#### XYT Trajectory (LINESTRINGM)
Fixed vertical coordinate, 100 samples along trajectory:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/trajectory?parameter-name=temperature&coords=LINESTRINGM(14.74 43.44 1611036000, 9.39 46.89 1611039600, 14.42 48.05 1611043200, 7.66 51.4 1611046800, 7.1 55.9 1611050400, 2.31 53.72 1611054000)&resolution=100&z=850&f=CoverageJSON`

***Note: Before running this query, don't forget to update the time stamps in the trajectory specification to the present date. The server contains data only for the past two days.***

#### XYZT Trajectory (LINESTRINGZM)
4D trajectory, 100 samples along trajectory:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/trajectory?parameter-name=temperature&coords=LINESTRINGZM(14.74 43.44 1000 1611036000, 9.39 46.89 800 1611039600, 14.42 48.05 500 1611043200, 7.66 51.4 500 1611046800, 7.1 55.9 700 1611050400, 2.31 53.72 1000 1611054000)&resolution=100&f=CoverageJSON`

***Note: Before running this query, don't forget to update the time stamps in the trajectory specification to the present date. The server contains data only for the past two days.***

### Corridor
#### XY Corridor
A 2D corridor across a horizontal plane. Time and vertical coordinates are fixed (2021-07-13T18:00:00, 850 hPa)

- 50 samples taken along the corridor
- The corridor is 100 km wide, 5 samples taken in lateral dimension (25 km spacing)

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/corridor?parameter-name=temperature&datetime=2021-07-13T18:00:00&coords=LINESTRING(14.74 43.44, 9.39 46.89, 14.42 48.05, 7.66 51.4, 7.1 55.9, 2.31 53.72)&corridor-width=100000&resolution-x=5&resolution-y=50&z=850&f=CoverageJSON`

#### XYZ Corridor
A 3D corridor travelling in X, Y and Z dimensions. Fixed time coordinate (2021-07-13T18:00:00)

- 50 samples taken along the corridor
- The corridor is 100 km wide, 9 samples taken in lateral dimension
- The corridor is 100 hPa high, 5 samples taken in vertical dimension

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/corridor?parameter-name=temperature&datetime=2021-07-13T18:00:00&coords=LINESTRINGZ(14.74 43.44 1000, 9.39 46.89 800, 14.42 48.05 500, 7.66 51.4 500, 7.1 55.9 700, 2.31 53.72 1000)&corridor-width=100000&resolution-x=9&corridor-height=100&resolution-z=5&resolution-y=50&f=CoverageJSON`

#### XYT Corridor
A 3D corridor travelling in X, Y and T dimensions. Fixed vertical coordinate (850 hPa)

- 50 samples taken along the corridor
- The corridor is 100 km wide, 9 samples taken in lateral dimension

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/corridor?parameter-name=temperature&coords=LINESTRINGM(14.74 43.44 1626199200, 9.39 46.89 1626202800, 14.42 48.05 1626206400, 7.66 51.4 1626210000, 7.1 55.9 1626213600, 2.31 53.72 1626217200)&corridor-width=100000&resolution-x=5&z=850&resolution-y=50&f=CoverageJSON`

#### XYZT Corridor
A corridor travelling in all dimensions

- 50 samples taken along the corridor
- The corridor is 100 km wide, 9 samples taken in lateral dimension
- The corridor is 100 hPa high, 5 samples taken in vertical dimension

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/corridor?parameter-name=temperature&coords=LINESTRINGZM(14.74 43.44 1000 1626199200, 9.39 46.89 800 1626202800, 14.42 48.05 500 1626206400, 7.66 51.4 500 1626210000, 7.1 55.9 700 1626213600, 2.31 53.72 1000 1626217200)&corridor-width=100000&resolution-x=9&corridor-height=100&resolution-z=5&resolution-y=50&f=CoverageJSON`