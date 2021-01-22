# Implementations of OGC API - EDR

## Overview

This page points to servers and clients implementing the OGC API - Environmental Data Retrieval standard.

Modern web browsers can, of course, act as clients.

To help promote OGC API standards and their implementations, implementers of OGC API standards are encouraged to register their implementations on the Programmable Web API Directory (https://www.programmableweb.com/add/api), in addition to registering at the OGC Compliance Database (https://www.ogc.org/resource/products/registration). 

These are the implementations that were used for the development of the standard:
1. [UK Met Office](http://labs.metoffice.gov.uk/edr/)              
     [Further details](#uk-met-office) 
1. [US NWS](https://data-api.mdl.nws.noaa.gov/EDR-API)       
     [Further details](#us-national-weather-service)
1. [IBL](https://ogcie.iblsoft.com/edr)      
     [Further details](#ibl-software-engineering)
1. [Wuhan University](http://geos.whu.edu.cn/whu-edr-demo/)       
     [Further details](#wuhan-university)
1. ESRI Image Server facade      
     [Further details](#esri-image-server-facade)
1. [USGS, Monitoring Networks wiki page mockup](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/wiki/Monitoring-network-mockup)      
     [Further details](#us-geological-survey)

Further implementations are planned or have been proposed for 2021: 
1. Unidata OpenDAP/THREDDS enhancement
1. NASA/JPL enhancement to Extensible Data Gateway Environment (EDGE)

Several other organisations, such as the European Centre for Medium-range Weather Forecasts (ECWMF), British Antarctic Survey (BAS)
and the British Oceanographic Data Centre (BODC) and others, are currently waiting until the full formal standard is published before committing resources.

## Implementations

### UK Met Office
Servers:
- [Example Server](http://labs.metoffice.gov.uk/edr/) developed by Mark Burgoyne.

Clients:
- [Example Client](http://labs.metoffice.gov.uk/edr/static/html/query.html)

Server description: implemented using python supports point, radius, area, trajectory and location queries

Client description:

#### Sample requests
- position: `http://labs.metoffice.gov.uk/edr/collections/terrain_tiles/position?coords=POINT(101.896366 45.209662)&parameter-name=Height&crs=CRS84&f=CoverageJSON`
- area: http://labs.metoffice.gov.uk/edr/collections/global_pop_density/area?coords=POLYGON((-3.652394 51.373721,-3.511786 50.264415,-1.973894 50.499557,-2.114501 51.73946,-3.652394 51.373721))&parameter-name=Pop_Density&crs=CRS84&f=CoverageJSON
- radius:  http://labs.metoffice.gov.uk/edr/collections/global_pop_density/radius?coords=POINT(-0.104939 51.513418)&within=30&within-units=km&parameter-name=Pop_Density&crs=CRS84&f=CoverageJSON
- trajectory: `http://labs.metoffice.gov.uk/edr/collections/terrain_tiles/trajectory?coords=LINESTRING(-3.519 50.737,-3.511 50.745,-3.504 50.753,-3.496 50.762,-3.489 50.77,-3.481 50.778,-3.473 50.786,-3.466 50.795,-3.458 50.803,-3.451 50.811,-3.443 50.819,-3.435 50.828,-3.428 50.836,-3.42 50.844,-3.412 50.853,-3.403 50.857,-3.392 50.859,-3.381 50.861,-3.37 50.863,-3.359 50.865,-3.348 50.867,-3.336 50.869,-3.325 50.871,-3.314 50.873,-3.303 50.875,-3.292 50.877,-3.281 50.879,-3.27 50.881,-3.259 50.883,-3.248 50.885,-3.237 50.887,-3.226 50.889,-3.215 50.89,-3.204 50.892,-3.192 50.894,-3.181 50.896,-3.17 50.898,-3.159 50.9,-3.148 50.902,-3.137 50.904,-3.126 50.906,-3.115 50.908,-3.104 50.91,-3.093 50.912,-3.082 50.914,-3.071 50.916,-3.06 50.918,-3.049 50.92,-3.048 50.931,-3.046 50.943,-3.045 50.954,-3.043 50.965,-3.042 50.976,-3.041 50.987,-3.039 50.998,-3.038 51.009,-3.036 51.021,-3.035 51.032,-3.034 51.043,-3.032 51.054,-3.031 51.065,-3.029 51.076,-3.028 51.088,-3.027 51.099,-3.025 51.11,-3.024 51.121,-3.022 51.132,-3.021 51.143,-3.02 51.155,-3.018 51.165,-3.007 51.165,-2.995 51.165,-2.984 51.165,-2.973 51.165,-2.962 51.165,-2.95 51.164,-2.939 51.164,-2.928 51.164,-2.917 51.164,-2.906 51.164,-2.894 51.164,-2.883 51.163,-2.872 51.163,-2.861 51.163,-2.849 51.163,-2.838 51.163)&parameter-name=Height&crs=CRS84&f=CoverageJSON`

#### Sample workflows
- sample URLs
- command line invocations
- code snippets

### US National Weather Service
Servers:
- [Example Server](https://data-api.mdl.nws.noaa.gov/EDR-API) developed by Shane Mill

Clients:
- [Example Client](https://data-api.mdl.nws.noaa.gov/EDR-CLIENT-API)

Server description: implemented using `pygeoapi` to provide a visual interface client. 
 Supports position, area, and cube queries. Provides schema support for CoverageJSON, JSON, 
 text, XML (IWXXM), and GRIB. Implementation uses open source software such as Flask, Xarray,
 Dask, and Zarr to name a few.
 
Client description: A series of simple clients demonstrating the feature extraction of a position 
  time series with visualization of the data in the form of a plotly graph. Demonstrates the ability
  to extract data using structured EDR-API requests from a variety of data sources and systems.

#### Sample requests
- position query: `https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_Ground_or_water_surface/instance/00z/position?coords=POINT(-89.331642 41.803319)&parametername=TMP_P0_L1_GLL0&datetime=2021-01-14T00:00:00/2021-01-14T18:00:00&crs=EPSG:4326&interpolation=nearest_neighbor&f=CoverageJSON`
- area query: `https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_Ground_or_water_surface/instance/00z/area?coords=POLYGON((-101.669985 54.012139,-116.184261 36.029225,-79.738717 25.623898,-62.986553 49.54781,-101.669985 54.012139))&parametername=TMP_P0_L1_GLL0&datetime=2021-01-14T00:00:00/2021-01-14T12:00:00&crs=EPSG:4326&interpolation-x=nearest_neighbor&interpolation-y=nearest_neighbor&f=CoverageJSON`
- cube query: `https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_Ground_or_water_surface/instance/00z/cube?coords=POLYGON((-100.135432 26.033864,-100.135432 52.365371,-66.511224 52.365371,-66.511224 26.033864,-100.135432 26.033864))&parametername=TMP_P0_L1_GLL0&datetime=2021-01-14T00:00:00/2021-01-14T18:00:00&crs=EPSG:4326&interpolation-x=nearest_neighbor&interpolation-y=nearest_neighbor&f=CoverageJSON`

#### Sample workflows
- sample URLs
- command line invocations
- code snippets

### IBL Software Engineering

Servers:

- [https://ogcie.iblsoft.com/edr](https://ogcie.iblsoft.com/edr)

Server description:

- Serves live GFS model data and live SYNOP, TEMP and METAR reports
- Implements point, radius, area, cube and trajectory query

#### Sample requests
:warning: ***The server contains live data not older than two days. Therefore, before you execute the queries below, please update instance IDs (model run) as well as 'date-time' URL parameters to the present date, for example:***

/edr/collections/GFS_isobaric/instances/**20210119T000000Z**/position?parameter-name=1000000_spec:regular&date-time=**2021-01-19T09:00:00**&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON

#### Position
##### Single Point
GFS 850 hPa temperature in Bratislava at 2021-01-19 09:00:00 UTC:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON`

##### Vertical Profile
GFS temperature in Bratislava at 2021-01-19 09:00 UTC, all available vertical levels:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=../..&f=CoverageJSON`

##### Time Series
GFS 850 hPa temperature in Bratislava from 2021-01-19 00:00 UTC until 2021-01-20 00:00 UTC @ 1h step:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T00:00:00/PT1H/25&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON`

#### Radius
Air temperature, wind speed and wind direction from METARs within 100 km radius around Bratislava, 24h interval:

`https://ogcie.iblsoft.com/edr/collections/metar/radius?parameter-name=station,validity,air-temperature,wind-speed,wind-direction&coords=POINT(17.21 48.18)&within=100&within-units=km&date-time=2021-01-19T00:00:00/2021-01-20T00:00:00&f=KernelTSV`

#### Area
##### Single Time and Level - Native Resolution
GFS wind (U and V component) within Slovakia at 2020-01-19 06:00 UTC, 850 hPa:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2`

##### Single Time and Level - Oversampled
The same as above but with higher spatial resolution:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&resolution-x=100&resolution-y=50&z=850&f=GRIB2`

##### Extruded in Vertical Dimension (Vertical Profile)
Wind (U and V component) within Slovakia at 2021-01-19 06:00 UTC, all vertical layers up to 300 hPa:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=../300&f=GRIB2`

##### Extruded in Time Dimension (Time Series)
Wind (U and V component) within Slovakia, all available forecasts starting from 2021-01-19 06:00 UTC, 850 hPa:

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00/..&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2`

#### Cube
##### GFS Data Within 4D Cube - Native Resolution
- Model: GFS
- Parameter: Air Temperature
- Bounding Box: 16.82 - 22.57E; 47.73 - 49.62N
- Vertical Extent: 1000 hPa → 300 hPa
- Time Extent: 2021-01-19 06:00 UTC → 2021-01-20 06:00 UTC
- Output format: GRIB2

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/cube?parameter-name=1000000_spec:regular&coords=BOX(16.82 47.73, 22.57 49.62)&min-z=1000&max-z=300&date-time=2021-01-19T06:00:00/2021-01-20T06:00:00&f=GRIB2`

##### GFS Data Within 4D Cube - Oversampled
The same as above but with a denser sampling (in all dimensions):

`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/cube?parameter-name=1000000_spec:regular&coords=BOX(16.82 47.73, 22.57 49.62)&resolution-x=24&resolution-y=8&min-z=1000&max-z=300&resolution-z=10&date-time=2021-01-19T06:00:00/PT1H/25&f=GRIB2`

##### TEMP Within 4D Cube
- Parameters: Pressure, Geopotential Height, Air Temperature, Wind- Speed, Wind Direction
- Bounding Box: 16.82 - 22.57E; 47.73 - 49.62N
- Vertical Extent: 1000 hPa → 300 hPa
- Time Extent: 2021-01-18 06:00 UTC → 2021-01-20 06:00 UTC

`https://ogcie.iblsoft.com/edr/collections/temp-pressure/cube?parameter-name=station,validity,pressure,geopotential,air-temperature,wind-speed,wind-direction&coords=BOX(16.82 47.73, 22.57 49.62)&min-z=1000&max-z=300&date-time=2021-01-18T06:00:00/2021-01-20T06:00:00&f=KernelTSV`

#### Trajectory
##### XY Trajectory (LINESTRING)
`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&date-time=2021-01-19T06:00:00&coords=LINESTRING(14.74 43.44, 9.39 46.89, 14.42 48.05, 7.66 51.4, 7.1 55.9, 2.31 53.72)&z=850&f=CoverageJSON`

Tip: Add vertical interval to form a "curtain": `z=1000/300`

##### XYZ Trajectory (LINESTRINGZ)
`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&date-time=2021-01-19T06:00:00&coords=LINESTRINGZ(14.74 43.44 1000, 9.39 46.89 800, 14.42 48.05 500, 7.66 51.4 500, 7.1 55.9 700, 2.31 53.72 1000)&f=CoverageJSON`

##### XYT Trajectory (LINESTRINGM)
`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&coords=LINESTRINGM(14.74 43.44 1611036000, 9.39 46.89 1611039600, 14.42 48.05 1611043200, 7.66 51.4 1611046800, 7.1 55.9 1611050400, 2.31 53.72 1611054000)&z=850&f=CoverageJSON`

##### XYZT Trajectory (LINESTRINGZM)
`https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&coords=LINESTRINGZM(14.74 43.44 1000 1611036000, 9.39 46.89 800 1611039600, 14.42 48.05 500 1611043200, 7.66 51.4 500 1611046800, 7.1 55.9 700 1611050400, 2.31 53.72 1000 1611054000)&f=CoverageJSON`

### Wuhan University
Servers:
- [Example Server](http://geos.whu.edu.cn/whu-edr-demo/) developed by 上官博屹 (Boyi Shangguan), 胡磊 (Lei Hu), 高凡 (Fan Gao) under 乐鹏 教授 (Prof. Peng Yue).

Clients:
- [Example Client](http://geos.whu.edu.cn:8081/monitor-forecast-edr/) developed by 上官博屹 (Boyi Shangguan), 胡磊 (Lei Hu), 高凡 (Fan Gao) under 乐鹏 教授 (Prof. Peng Yue).

Server description: implemented using `pygeoapi` to provide a visual interface client. Supports position, area, trajectory and corridor queries.

Client description: a web application for flood disaster decision support, implemented with EDR API to query related data such as population, schools and villages after obtaining a typhoon trajectory/corridor or flood inundation area.

#### Sample requests
- position query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/position?coords=POINT(109.858046 19.230770)&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`
- area query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/area?coords=POLYGON((109.795906 19.259092,109.885383 19.264480,109.879889 19.168519,109.795906 19.259092))&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`
- trajectory query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/trajectory?coords=LINESTRING(109.298000 19.139979,109.589138 19.321511,109.891262 19.513198,110.198879 19.761534)&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`
- corridor query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/corridor?coords=LINESTRING(109.243069 18.968637,109.429836 19.150357,109.726467 19.311143,110.138454 19.476950)&corridor-width=1000&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`

#### Sample workflows
- sample URLs
- command line invocations
- code snippets
```
// Use Promise to send HTTP request, and analyse results together
Promise.all([
    $.ajax({
        url: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/area?coords=${rangeWkt}&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`,
        dataType: 'json'
    }),
]).then(function (result) {
    let sum = 0;
    result.forEach(value => {
        if (value.ranges !== undefined && value.ranges.population.values !== null) {
            value.ranges.population.values.forEach(value => {
                if (value !== null) {
                    sum += value;
                }
            })
        }
    });
}
```

### ESRI Image Server facade
Servers:
-   Example Server currently not available. Proof-of-Concept developed by Pete Trevelyan and ESRI developers. Supports point and area queries. The server will be further developed to increase the supported EDR query patterns. 

Clients:
-   Example Client: There will be no specialist client created other than those already available. At the most basic level the server may be accessed using Swagger Hub that is invoked by the `home / address`.

Server description:
The server in a simple proxy server that translates EDR queries into the native ESRI Rest API for Image Server.

Client description: Not Applicable

#### Sample requests
-   The sample requests will be generated by using the Swagger Hub based on the YAML Swagger document that may be obtained using `/doc`

#### Sample workflows
 -   There is no need to support a semi-permanent server, as the proxy server will normally be set up by the user. 
 -   Command Line Invocations
If installed locally (The code will be available in GitHub) then a simple environment variable will hold the address of the ESRI Server. There is a README file that will give full instructions -   
 -   Code Snippets
The proxy is written using the Express - Node.js web application framework and may be invoked from the command line using the Node run command.

### US Geological Survey
Servers:
- [Example Server](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/wiki/Monitoring-network-mockup) Mock-up to demonstrate usage and compatibility of EDR API and Features API 

Clients:
- Example Client tbd

Server description: tbd

Client description: tbd

#### Sample requests
- tbd
- tbd

#### Sample workflows
- sample URLs
- command line invocations
- code snippets

---
