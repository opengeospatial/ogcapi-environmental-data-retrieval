# leaflet-coverage

This page shows an example how to add a CoverageJSON response to a map from a server implementing the CoverageJSON
Conformance Class of OGC API - EDR.

## Links

- Open the example in [Codepen](https://codepen.io/letmaik/pen/OXgPXQ)
- [leafet-coverage documentation](https://github.com/Reading-eScience-Centre/leaflet-coverage)

## Software version

This example uses covjson-reader 0.7.2.

## Required and supported Conformance classes

The API must support the [Core](http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core), [Queries](http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/queries] and [CoverageJSON](http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/covjson) conformance classes.

leaflet-coverage does not support OGC API - EDR, so the coverage data for each collection has to be accessed directly as CoverageJSON.

## Description

To add GeoJSON features accessed from an API implementing OGC API Features, access the features from a Features resource (relative path `collections/{collectionId}/items` from the Landing Page) with a limit value that is sufficient for the number of features in the collection. In this example, the URL is `https://demo.ldproxy.net/zoomstack/collections/airports/items?limit=100` to retrieve the airports in Great Britain. The response is a GeoJSON feature collection that can be added to the Leaflet map.

Here is an example using the Fetch API:

```javascript
CovJSON.read(
  "https://raw.githubusercontent.com/covjson/cookbook/master/examples/coverages/grid.covjson"
)
  .then(function (cov) {
    // work with Coverage object
    document.getElementById("coverage-type").innerHTML = cov.type;
    let parameters = [];
    for (param in cov._covjson.parameters) {
      parameters.push(param);
    }
    document.getElementById("parameters").innerHTML = parameters;
  })
  .catch(function (e) {
    // there was an error when loading the coverage
    console.log(e);
  });
```

Open the complete HTML document in [Codepen](https://codepen.io/tomkralidis/pen/yLMYVwL).
