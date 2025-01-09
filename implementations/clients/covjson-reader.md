# covjson-reader

This page shows an example how to read a CoverageJSON response from a server implementing the CoverageJSON
Conformance Class of OGC API - EDR.

## Links

- Open the example in [Codepen](https://codepen.io/tomkralidis/pen/yLMYVwL)
- [covjson-reader documentation](https://github.com/Reading-eScience-Centre/covjson-reader)

## Software version

This example uses covjson-reader 0.7.2.

## Required and supported Conformance classes

The API SHALL support the [Core](https://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core), [Queries](https://www.opengis.net/spec/ogcapi-common-1/1.0/conf/queries] and [CoverageJSON](https://www.opengis.net/spec/ogcapi-common-1/1.0/conf/covjson) conformance classes.

covjson-reader does not support OGC API - EDR, so the coverage data for each collection has to be accessed directly as CoverageJSON.

## Description

To add CoverageJSON features accessed from an API implementing OGC API - EDR, access the collection via a query resource (relative path `/collections/{collectionId}/position`. The is a CoverageJSON representation that can be added to the Leaflet map.

Here is an example using sample data from the CoverageJSON cookbook:

```javascript
var map = L.map('map', { center: [10, 0], zoom: 2 })
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map)

var layers = L.control.layers(null, null, {collapsed: false}).addTo(map)

var dataUrl = 'https://raw.githubusercontent.com/covjson/cookbook/master/examples/coverages/grid.covjson'

var layer
CovJSON.read(dataUrl).then(function (coverage) {
  layer = C.dataLayer(coverage, {parameter: 'temperature'})
    .on('afterAdd', function () {
      C.legend(layer).addTo(map)
      map.fitBounds(layer.getBounds())
    })
    .addTo(map)
  layers.addOverlay(layer, 'Temperature')
})

map.on('click', function (e) {
  new C.DraggableValuePopup({
    layers: [layer]
  }).setLatLng(e.latlng).openOn(map)
})
```

Open the complete HTML document in [Codepen](https://codepen.io/letmaik/pen/OXgPXQ)
