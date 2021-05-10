# pygeoapi

[pygeoapi](https://pygeoapi.io) is a Python server implementation of the
OGC API suite of standards. The project emerged as part of the next generation
OGC API efforts in 2018 and provides the capability for organizations to deploy
a RESTful OGC API endpoint using OpenAPI, GeoJSON, and HTML. pygeoapi is open
source and released under an MIT license.  pygeoapi is an [OGC Reference Implementation](https://www.ogc.org/resource/products/details/?pid=1663).

pygeoapi implements the current EDR candidate standard with a robust plugin
mechanism, allowing for flexible integration of SpatioTemporal data into the
OGC API family of standards, including EDR.

## Demo deployment

The main pygeoapi demonstrations are available at https://demo.pygeoapi.io.
Here, we will use the [latest GitHub master demo](https://demo.pygeoapi.io/master)
to demonstrate EDR functionality against [ICOADS](https://icoads.noaa.gov)
data.

- Landing page: https://demo.pygeoapi.io/master
- OpenAPI document (Swagger): https://demo.pygeoapi.io/master/openapi
  - see `icoads-sst` endpoints

Resources are available as HTML and CoverageJSON. Add `f=json` or `f=html`
to override HTTP content negotiation.

Sample requests:
- Conformance: https://demo.pygeoapi.io/master/conformance
- Collections: https://demo.pygeoapi.io/master/collections
- The ICOADS-SST collection: https://demo.pygeoapi.io/master/collections/icoads-sst
  - see `parameter-names` object for parameter names/definitions
- Position queries:
  - Specific point, all parameters: https://demo.pygeoapi.io/master/collections/icoads-sst/position?f=json&coords=POINT(33%2033)
  - Specific point, sea surface temperature (SST): https://demo.pygeoapi.io/master/collections/icoads-sst/position?f=json&coords=POINT(33%2033)&parameter-name=SST
  - Specific point, all parameters, temporal instant: https://demo.pygeoapi.io/master/collections/icoads-sst/position?f=json&coords=POINT(33%2033)&datetime=2000-01-16

More information about pygeoapi:
- [GitHub repository](https://github.com/geopython/pygeoapi)
