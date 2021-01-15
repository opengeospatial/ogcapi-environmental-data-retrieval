# Implementations of OGC API - EDR

## Overview

This page points to servers and clients implementing the OGC API - Environmental Data Retrieval standard.

Modern web browsers can, of course, act as clients.

To help promote OGC API standards and their implementations, implementers of OGC API standards are encouraged to register their implementations on the Programmable Web API Directory (https://www.programmableweb.com/add/api), in addition to registering at the OGC Compliance Database (https://www.ogc.org/resource/products/registration). 

These are the implementations that were used for the development of the standard:
1. [UK Met Office](http://labs.metoffice.gov.uk/edr2/)              
     [Further details](#uk-met-office) **This demonstration instance is being re-built more securely. (2021-01-12)**
1. [US NWS](https://data-api.mdl.nws.noaa.gov/EDR-API)       
     [Further details](#us-national-weather-service)
1. [IBL](https://ogcie.iblsoft.com/edr)      
     [Further details](#ibl)
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
- [Example Server](http://labs.metoffice.gov.uk/edr2/) developed by Mark Burgoyne.

Clients:
- [Example Client](#example-client)

 Server description: implemented using `pygeoapi` to provide a visual interface client. 
 Supports point, area and trajectory queries

Client description:

### Sample requests
- tbd
- tbd

### Sample workflows

- sample URLs
- command line invocations
- code snippets

### US National Weather Service
Servers:
- [Example Server](#example-server) developed by Shane Mill

Clients:
- [Example Client](#example-client)

Server description: implemented using `pygeoapi` to provide a visual interface client. 
 Supports point and area queries
 
Client description:

### Sample requests
- tbd
- tbd

### Sample workflows

- sample URLs
- command line invocations
- code snippets

### IBL Software Engineering

Servers:

- [https://ogcie.iblsoft.com/edr](https://ogcie.iblsoft.com/edr)

Server description:

- Serves live GFS model data and live SYNOP, TEMP and METAR reports
- Implements point, radius, area, cube and trajectory query

### Sample requests
:warning: ***The server contains live data not older than two days. Therefore, before you execute the queries below, please update instance IDs (model run) as well as 'date-time' URL parameters to the present date, for example:***

https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/**20210119T000000Z**/position?parameter-name=1000000_spec:regular&date-time=**2021-01-19T09:00:00**&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON

#### Position
##### Single Point
GFS 850 hPa temperature in Bratislava at 2021-01-19 09:00:00 UTC:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON)

##### Vertical Profile
GFS temperature in Bratislava at 2021-01-19 09:00 UTC, all available vertical levels:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=../..&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T09:00:00&coords=POINT(17.11 48.14)&z=../..&f=CoverageJSON)

##### Time Series
GFS 850 hPa temperature in Bratislava from 2021-01-19 00:00 UTC until 2021-01-20 00:00 UTC @ 1h step:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/
20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T00:00:00/PT1H/25&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/position?parameter-name=1000000_spec:regular&date-time=2021-01-19T00:00:00/PT1H/25&coords=POINT(17.11 48.14)&z=850&f=CoverageJSON)

#### Radius
Air temperature, wind speed and wind direction from METARs within 100 km radius around Bratislava, 24h interval:

[https://ogcie.iblsoft.com/edr/collections/metar/radius?parameter-name=station,validity,air-temperature,wind-speed,wind-direction&coords=POINT(17.21 48.18)&within=100&within-units=km&date-time=2021-01-19T00:00:00/2021-01-20T00:00:00&f=KernelTSV](https://ogcie.iblsoft.com/edr/collections/metar/radius?parameter-name=station,validity,air-temperature,wind-speed,wind-direction&coords=POINT(17.21 48.18)&within=100&within-units=km&date-time=2021-01-19T00:00:00/2021-01-20T00:00:00&f=KernelTSV)

#### Area
##### Single Time and Level - Native Resolution
GFS wind (U and V component) within Slovakia at 2020-01-19 06:00 UTC, 850 hPa:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2)

##### Single Time and Level - Oversampled
The same as above but with higher spatial resolution:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&resolution-x=100&resolution-y=50&z=850&f=GRIB2](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&resolution-x=100&resolution-y=50&z=850&f=GRIB2)

##### Extruded in Vertical Dimension (Vertical Profile)
Wind (U and V component) within Slovakia at 2021-01-19 06:00 UTC, all vertical layers up to 300 hPa:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=../300&f=GRIB2](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=../300&f=GRIB2)

##### Extruded in Time Dimension (Time Series)
Wind (U and V component) within Slovakia, all available forecasts starting from 2021-01-19 06:00 UTC, 850 hPa:

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00/..&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric_3/instances/20210119T000000Z/area?parameter-name=1000514_spec:regular,1000515_spec:regular&date-time=2021-01-19T06:00:00/..&coords=POLYGON((17.98 49.08, 16.94 48.70, 16.95 48.01, 17.96 47.63, 18.99 47.80, 21.00 48.56, 22.25 48.39, 22.75 49.14, 21.31 49.51, 20.15 49.36, 20.10 49.19, 19.69 49.22, 19.48 49.63, 18.94 49.56))&z=850&f=GRIB2)

#### Cube
##### GFS Data Within 4D Cube - Native Resolution
- Model: GFS
- Parameter: Air Temperature
- Bounding Box: 16.82 - 22.57E; 47.73 - 49.62N
- Vertical Extent: 1000 hPa → 300 hPa
- Time Extent: 2021-01-19 06:00 UTC → 2021-01-20 06:00 UTC
- Output format: GRIB2

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/cube?parameter-name=1000000_spec:regular&coords=BOX(16.82 47.73, 22.57 49.62)&min-z=1000&max-z=300&date-time=2021-01-19T06:00:00/2021-01-20T06:00:00&f=GRIB2](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/cube?parameter-name=1000000_spec:regular&coords=BOX(16.82 47.73, 22.57 49.62)&min-z=1000&max-z=300&date-time=2021-01-19T06:00:00/2021-01-20T06:00:00&f=GRIB2)

##### GFS Data Within 4D Cube - Oversampled
The same as above but with a denser sampling (in all dimensions):

[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/cube?parameter-name=1000000_spec:regular&coords=BOX(16.82 47.73, 22.57 49.62)&resolution-x=24&resolution-y=8&min-z=1000&max-z=300&resolution-z=10&date-time=2021-01-19T06:00:00/PT1H/25&f=GRIB2](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/cube?parameter-name=1000000_spec:regular&coords=BOX(16.82 47.73, 22.57 49.62)&resolution-x=24&resolution-y=8&min-z=1000&max-z=300&resolution-z=10&date-time=2021-01-19T06:00:00/PT1H/25&f=GRIB2)

##### TEMP Within 4D Cube
- Parameters: Pressure, Geopotential Height, Air Temperature, Wind- Speed, Wind Direction
- Bounding Box: 16.82 - 22.57E; 47.73 - 49.62N
- Vertical Extent: 1000 hPa → 300 hPa
- Time Extent: 2021-01-18 06:00 UTC → 2021-01-20 06:00 UTC

[https://ogcie.iblsoft.com/edr/collections/temp-pressure/cube?parameter-name=station,validity,pressure,geopotential,air-temperature,wind-speed,wind-direction&coords=BOX(16.82 47.73, 22.57 49.62)&min-z=1000&max-z=300&date-time=2021-01-18T06:00:00/2021-01-20T06:00:00&f=KernelTSV](https://ogcie.iblsoft.com/edr/collections/temp-pressure/cube?parameter-name=station,validity,pressure,geopotential,air-temperature,wind-speed,wind-direction&coords=BOX(16.82 47.73, 22.57 49.62)&min-z=1000&max-z=300&date-time=2021-01-18T06:00:00/2021-01-20T06:00:00&f=KernelTSV)

#### Trajectory
##### XY Trajectory (LINESTRING)
[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&date-time=2021-01-19T06:00:00&coords=LINESTRING(14.74 43.44, 9.39 46.89, 14.42 48.05, 7.66 51.4, 7.1 55.9, 2.31 53.72)&z=850&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&date-time=2021-01-19T06:00:00&coords=LINESTRING(14.74 43.44, 9.39 46.89, 14.42 48.05, 7.66 51.4, 7.1 55.9, 2.31 53.72)&z=850&f=CoverageJSON)

Tip: Add vertical interval to form a "curtain": z=1000/300

##### XYZ Trajectory (LINESTRINGZ)
[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&date-time=2021-01-19T06:00:00&coords=LINESTRINGZ(14.74 43.44 1000, 9.39 46.89 800, 14.42 48.05 500, 7.66 51.4 500, 7.1 55.9 700, 2.31 53.72 1000)&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&date-time=2021-01-19T06:00:00&coords=LINESTRINGZ(14.74 43.44 1000, 9.39 46.89 800, 14.42 48.05 500, 7.66 51.4 500, 7.1 55.9 700, 2.31 53.72 1000)&f=CoverageJSON)

##### XYT Trajectory (LINESTRINGM)
[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&coords=LINESTRINGM(14.74 43.44 1611036000, 9.39 46.89 1611039600, 14.42 48.05 1611043200, 7.66 51.4 1611046800, 7.1 55.9 1611050400, 2.31 53.72 1611054000)&z=850&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&coords=LINESTRINGM(14.74 43.44 1611036000, 9.39 46.89 1611039600, 14.42 48.05 1611043200, 7.66 51.4 1611046800, 7.1 55.9 1611050400, 2.31 53.72 1611054000)&z=850&f=CoverageJSON)

##### XYZT Trajectory (LINESTRINGZM)
[https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&coords=LINESTRINGZM(14.74 43.44 1000 1611036000, 9.39 46.89 800 1611039600, 14.42 48.05 500 1611043200, 7.66 51.4 500 1611046800, 7.1 55.9 700 1611050400, 2.31 53.72 1000 1611054000)&f=CoverageJSON](https://ogcie.iblsoft.com/edr/collections/GFS_isobaric/instances/20210119T000000Z/trajectory?parameter-name=1000000_spec:regular&coords=LINESTRINGZM(14.74 43.44 1000 1611036000, 9.39 46.89 800 1611039600, 14.42 48.05 500 1611043200, 7.66 51.4 500 1611046800, 7.1 55.9 700 1611050400, 2.31 53.72 1000 1611054000)&f=CoverageJSON)

### Wuhan University
Servers:
- [Example Server](#example-server) developed by 博屹 上官 (Boyi Shangguan), 胡 磊 (Hu Lei), 高 凡 (Fan Gao) under 乐 鹏 教授 (Prof. Yue Peng).

Clients:
- [Example Client](#example-client)

Server description: implemented using `pygeoapi` to provide a visual interface client. Supports point, area, trajectory and corridor queries

Client description:

### Sample requests
- tbd
- tbd

### Sample workflows

- sample URLs
- command line invocations
- code snippets

### ESRI Image Server facade
Servers:
- [Example Server](#example-server) Proof-of-Concept developed by Pete Trevelyan and ESRI developers. Supports point and area queries.

Clients:
- [Example Client](#example-client)

Server description: 

Client description:

### Sample requests
- tbd
- tbd

### Sample workflows

- sample URLs
- command line invocations
- code snippets

### US Geological Survey
Servers:
- [Example Server](#example-server) Mock-up to demonstrate usage and compatibility of EDR API and Features API 

Clients:
- [Example Client](#example-client)

Server description:

Client description:

### Sample requests
- tbd
- tbd

### Sample workflows

- sample URLs
- command line invocations
- code snippets

---
