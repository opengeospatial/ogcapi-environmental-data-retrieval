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

### Sample requests
- position query: `https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_Ground_or_water_surface/instance/00z/position?coords=POINT(-89.331642 41.803319)&parametername=TMP_P0_L1_GLL0&datetime=2021-01-14T00:00:00/2021-01-14T18:00:00&crs=EPSG:4326&interpolation=nearest_neighbor&f=CoverageJSON`
- area query: `https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_Ground_or_water_surface/instance/00z/area?coords=POLYGON((-101.669985 54.012139,-116.184261 36.029225,-79.738717 25.623898,-62.986553 49.54781,-101.669985 54.012139))&parametername=TMP_P0_L1_GLL0&datetime=2021-01-14T00:00:00/2021-01-14T12:00:00&crs=EPSG:4326&interpolation-x=nearest_neighbor&interpolation-y=nearest_neighbor&f=CoverageJSON`
- cube query: `https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_Ground_or_water_surface/instance/00z/cube?coords=POLYGON((-100.135432 26.033864,-100.135432 52.365371,-66.511224 52.365371,-66.511224 26.033864,-100.135432 26.033864))&parametername=TMP_P0_L1_GLL0&datetime=2021-01-14T00:00:00/2021-01-14T18:00:00&crs=EPSG:4326&interpolation-x=nearest_neighbor&interpolation-y=nearest_neighbor&f=CoverageJSON`

### Sample workflows

- sample URLs
- command line invocations
- code snippets

### IBL
Servers:
- [Example Server](#example-server) developed by Igor Andruska, Pavol Navotny and colleagues

Clients:
- [Example Client](#example-client)

Server description: Supports point, area and trajectory queries.

### Sample requests
- tbd
- tbd

### Sample workflows

- sample URLs
- command line invocations
- code snippets

### Wuhan University
Servers:
- [Example Server](http://geos.whu.edu.cn/whu-edr-demo/) developed by 上官博屹 (Boyi Shangguan), 胡磊 (Lei Hu), 高凡 (Fan Gao) under 乐鹏 教授 (Prof. Peng Yue).

Clients:
- [Example Client](http://geos.whu.edu.cn:8081/monitor-forecast-edr/) developed by 上官博屹 (Boyi Shangguan), 胡磊 (Lei Hu), 高凡 (Fan Gao) under 乐鹏 教授 (Prof. Peng Yue).

Server description: implemented using `pygeoapi` to provide a visual interface client. Supports position, area, trajectory and corridor queries.

Client description: a web application for flood disaster decision support, implemented with EDR API to query related data such as population, schools and villages after obtaining a typhoon trajectory/corridor or flood inundation area.

### Sample requests
- position query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/position?coords=POINT(109.858046 19.230770)&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`
- area query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/area?coords=POLYGON((109.795906 19.259092,109.885383 19.264480,109.879889 19.168519,109.795906 19.259092))&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`
- trajectory query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/trajectory?coords=LINESTRING(109.298000 19.139979,109.589138 19.321511,109.891262 19.513198,110.198879 19.761534)&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`
- corridor query: `http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/corridor?coords=LINESTRING(109.243069 18.968637,109.429836 19.150357,109.726467 19.311143,110.138454 19.476950)&corridor-width=1000&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON`

### Sample workflows

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
