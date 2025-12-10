# OGC-EDR Demo Server Implementation by Edwin Gichuru

This implementation is a work in progress and may not conform to the conformance classes advertised. If such an error is found, feel free to create an issue or reach out via e-mail.

This implementation conditionally supports queries based on the data type of the source data or a personal decision. Available output formats also depend on the data type of source data although most collections do support CoverageJSON.

For example, raster datasets may support `resolution-[x|y|z]` parameter queries but vector ones don't because it is easy to sample raster datasets.

It should support v1.0.0, v1.0.1, v1.1.0 and Part 2: Publish/Subscribe.

[Project Github Repo](http://github.com/murithigeo/ogc-edr-api)

## Demo Deployment

- Landing Page: https://ogc-edr-api.murithigeo.deno.net/
- OpenAPI Document: https://ogc-edr-api.murithigeo.deno.net/api
- Interactive Web Console (Like Swagger): https://ogc-edr-api.murithigeo.deno.net/api.html
- AsyncAPI Document: https://ogc-edr-api.murithigeo.deno.net/asyncapi
- Interactive Web Console for AsyncAPI (Full Support by Scalar Pending): https://ogc-edr-api.murithigeo.deno.net/asyncapi.html

## Part 1

### Instances

- All instances: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/instances`

- Speficic instance: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/instances/Africa`

### Position

- Without Subsetting: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/position?coords=MULTIPOINT(36.804199 -1.285293, 39.660645 -4.050577)`
- Within instance: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/instances/2025-09-01/position?coords=MULTIPOINT(36.804199 -1.285293, 39.660645 -4.050577)`

### Cube

- Without subsetting: `https://ogc-edr-api.murithigeo.deno.net/fapar-anomaly/cube?bbox=32,-2,34,2`

- Within instance: `https://ogc-edr-api.murithigeo.deno.net/fapar-anomaly/instances/2025-09-01/cube?bbox=32,-2,34,2`

### Corridor

- Without subsetting: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/corridor?coords=LINESTRING (36.815186 -1.30726, 39.70459 -4.039618)&corridor-width=100&corridor-height=10&height-units=meters&width-units=meters`

- Within Instance: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/instances/2025-09-01/corridor?coords=LINESTRING (36.815186 -1.30726, 39.70459 -4.039618)&corridor-width=100&corridor-height=10&height-units=meters&width-units=meters`

### Trajectory

### Radius

- Without Subsetting: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/radius?coords=MULTIPOINT(36.804199 -1.285293, 39.660645 -4.050577)&within=100&within-units=meters`

- Within Instance: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/instances/2025-09-01/radius?coords=MULTIPOINT(36.804199 -1.285293, 39.660645 -4.050577)&within=100&within-units=meters`

### Items

- Without Subsetting
  - All Items: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/items?bbox=32,-2,34,2`
  - Specific Item: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/items/Mount%20Kenya`
- Within Instance:
  - All Items: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/instances/Africa/items?bbox=32,-2,34,2`
  - Specific Item: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/instances/Africa/items/Mount%20Kenya`

### Locations

- Without Subsetting:
  - All Locations: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/locations`
  - Data Within Location: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/locations/Kenya`
- Within Instance:
  - All Locations: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/instances/Africa/locations`
  - Data Within Multiple Locations: `https://ogc-edr-api.murithigeo.deno.net/collections/mountains/instances/Africa/locations/Kenya,Uganda,Tanzania`

### Area

- Without Subsetting: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/area?coords=POLYGON ((36.293335 -1.126026, 36.436157 -1.45004, 36.903076 -1.466515, 36.87561 -1.158979, 36.77124 -0.917319, 36.293335 -1.126026))`

- Within Instance: `https://ogc-edr-api.murithigeo.deno.net/collections/fapar-anomaly/instances/2025-09-01/area?coords=POLYGON ((36.293335 -1.126026, 36.436157 -1.45004, 36.903076 -1.466515, 36.87561 -1.158979, 36.77124 -0.917319, 36.293335 -1.126026))`

## Part 2: Publish/Subscribe Workflow

This relies on WebSockets. This part of the implementation is arguably simple because it does not require additional web packages by the client. One only needs a database that can cache notifications/messages and allows watching specific records.

When the client first connects to the hub, all cached messages are sent by the server. The uuid(id) of each message sent during the session is cached so that the same messages are not sent repeatedly during the session. When a watch event is detected on the server, the message is sent to the client.

To receive updates on a specific channel, initialize a new WebSockets to a channel i.e.

Init the WebSocket
`const socket= new WebSocket("https://ogc-edr-api.murithigeo.deno.net/collections/openmeteo-hourly")`

Receive messages
`socket.onmessage=(e:MessageEvent<MessageType>)=>{const data=JSON.parse(e.data);//Do something with the data}`

NOTE: A WebSocket can be open when the protocol is set to `https`/`wss` or `ws`/`http`

### Supported WebSocket Paths

- All Collections: `wss://ogc-edr-api.murithigeo.deno.net/collections`
- Specific Collection: `wss://ogc-edr-api.murithigeo.deno.net/collections/openmeteo-hourly`

To showcase this part of the implementation, data from [Open-Meteo](https://open-meteo.com) is used. On a hourly interval, data is queried for start of current hour and cached in memory.

- All Instances: `wss://ogc-edr-api.murithigeo.deno.net/collections/openmeteo-hourly/instances`

The pattern for each instanceId (hour) is `yyyy-MM-dd'T'HH:mm`

- Current Hour: `wss://ogc-edr-api.murithigeo.deno.net/collections/openmeteo-hourly/instances/<instanceId>`

- All Items in Instance: `wss://ogc-edr-api.murithigeo.deno.net/collections/openmeteo-hourly/instances/<instanceId>/items`

- Specific Item in Instance: `wss://ogc-edr-api.murithigeo.deno.net/collections/openmeteo-hourly/instances/<instanceId>/items/GHCND:KE000063740`

## NOTES

## NOTES

The approach is fairly simple.
For vector datasets, some query_types such as radius, corridor, trajectory, etc will use a geometry intersection check.

For raster datasets, a bounding box of the coords/geometry will be generated, regular sample points will be generated within the bounding box. For radius, area, etc, a geometry intersection check is also carried for the generated points to ensure conformance with shape of geometry. The raster is then sampled.

### 6 Item Bounding Boxes

If a 6 item bounding box is declared, then the 3rd & 6th element are considered the elevation limits of the response. This is overridden if the z parameter is declared

### LINESTRING[Z][M]

If a LINESTRING Z or LINESTRING ZM is requested and no z parameter is declared, the included elevation values are used to constrain the response. Only values whose z value appears in the wkt string will be returned.

This also applies to LINESTRING M or LINESTRING ZM coords.
