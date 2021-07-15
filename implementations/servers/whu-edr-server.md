# WHU EDR-API Server Implementation

The WHU implementation of the EDR-API was originally forked from pygeoapi and customized code was developed to prototype the WHU's use cases.
The implementation supports position, area, trajectory, and corridor queries of raster data in GeoTIFF format, and area query of vector data in GeoJSON format.


## Demo deployment

- Landing page: http://geos.whu.edu.cn/whu-edr-demo
- OpenAPI document (Swagger): http://geos.whu.edu.cn/whu-edr-demo/openapi?f=html


Sample requests:
- Position query of raster data (population density in POINT(109.858046 19.230770) of a province of China at 2019-01-01 00:00:00 UTC, supports CoverageJSON):
  - http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/position?coords=POINT(109.858046 19.230770)&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON

- Area query of raster data (population density in a polygon area of a province of China at 2019-01-01 00:00:00 UTC, supports CoverageJSON):
  - http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/area?coords=POLYGON((109.795906 19.259092,109.885383 19.264480,109.879889 19.168519,109.795906 19.259092))&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON
  
- Area query of vecter data (village pois in a polygon area of a province of China at 2019-01-01 00:00:00 UTC, supports GeoJSON):
  - http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_village/area?coords=POLYGON((109.910038 19.361681,109.985569 19.359089,109.993808 19.243736,109.897678 19.252164,109.910038 19.361681))&datetime=2019-01-01T00:00:00&parameter-name=village&interpolation=nearest_neighbour&f=GeoJSON

- Trajectory query of raster data (population density in a typhoon trjectory intersecting a province of China at 2019-01-01 00:00:00 UTC, supports CoverageJSON):
  - http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/trajectory?coords=LINESTRING(109.298000 19.139979,109.589138 19.321511,109.891262 19.513198,110.198879 19.761534)&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON

- Corridor query of raster data(population density in a typhoon corridor intersecting a province of China at 2019-01-01 00:00:00 UTC, supports CoverageJSON):
  - http://geos.whu.edu.cn/whu-edr-demo/collections/hainan_pop/corridor?coords=LINESTRING(109.243069 18.968637,109.429836 19.150357,109.726467 19.311143,110.138454 19.476950)&corridor-width=1000&datetime=2019-01-01T00:00:00&parameter-name=population&interpolation=nearest_neighbour&f=CoverageJSON


