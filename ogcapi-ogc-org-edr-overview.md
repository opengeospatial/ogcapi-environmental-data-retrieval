# OGC API - Environmental Data Retrieval

[OGC API standards](https://ogcapi.ogc.org/) define modular API building blocks to spatially enable Web APIs
in a consistent way. [OpenAPI](http://openapis.org) is used to define the reusable
API building blocks with responses in JSON and HTML.

The OGC API family of standards is organized by resource type. The draft OGC API - Environmental Data Retrieval standard defines an Environmental Data Retrieval (EDR) API with two goals:

1.	To allow clients to retrieve a subset of data created by the API in response to a standardized, coordinate orientated, query pattern;
2.	To provide 'building blocks' allowing the construction of more complex applications.

The EDR API can be considered a 'Sampling API'. The query creates a discrete sampling geometry against the Environmental Data resource of a relatively persistent data store. The query and its response are transient resources, which could be made persistent for re-use if required.

The functionality provided by EDR query patterns could be realized through specific implementation of the SOS (and to some extent WCS) from the OGC Web Services family of (XML-based) standards. EDR introduces a streamlined JSON-based OGC API implementation of building blocks that could be used for many of the same use cases addressed by SOS and WCS in the past.


## Overview of OGC API - Environmental Data Retrieval

The API provides access to Environmental Data Retrieval.

The following is an overview of the paths to resources offered by implementations of this standard, where `{root}` is Base URI for the API server, `{collectionId}` is an identifier for a specific collection of data, `{instanceId}` is an identifier for a specific version or instance of a collection of data, and `{queryType}` is an identifier for a specific query pattern to retrieve data from a specific collection of data.

```
GET {root}/collections
```

Metadata describing the collections of data available from this API.

```
GET {root}/collections/{collectionId}
```

Metadata describing the collection of data which has the unique identifier `{collectionId}`.

The metadata describes basic information about the geospatial data collection, like its id and description, as well as the spatial and temporal extents of all the data contained.

```
GET /collections/{collectionId}/items/{featureId}
```

Returns a single 'feature' - something in the real-world (a building,
a stream, a county, etc.) that typically is described by a geometry plus other properties. The EDR API's Items query is an OGC API - Features endpoint that may be used to catalog pre-existing EDR sampling features.


```
GET {root}/collections/{collectionId}/{queryType}
```

Retrieves data according to the query pattern. Query resources are spatial queries which support the operation of the API or the access and use of the Environmental Data resources.


```
GET {root}/collections/{collectionId}/instances
```

Retrieve metadata about instances of a collection.

```
GET {root}/collections/{collectionId}/instances/{instanceId}
```

Retrieve metadata from a specific instance of a collection which has the unique identifier `{instanceId}`.
