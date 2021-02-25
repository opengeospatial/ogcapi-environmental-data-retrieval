# Candidate specification for the Environmental Data Retrieval API

[<img src="http://www.opengeospatial.org/pub/www/files/OGC_Logo_2D_Blue_x_0_0.png" width="200"/>](https://www.opengeospatial.org)

This is the GitHub repository of the [OGC Environmental Data Retrieval API Standard Working Group (EDR API SWG)](https://www.opengeospatial.org/projects/groups/edr-apiswg).

The **OGC API - Environmental Data Retrieval** candidate standard is part of the OGC API suite of standards. [OGC API standards](https://ogcapi.ogc.org) define modular API building blocks to spatially enable Web APIs in a consistent way. [OpenAPI](http://openapis.org) is used to define the reusable API building blocks.

### EDR API Query Patterns
The EDR API allows a query, constructed of a spatio-temporal pattern, to retrieve data just for that pattern, from a data collection resource. Each of these patterns is optional, but a compliant API should implement at least one of them. 

The main patterns are:
- **1 - Position**: Retrieve data for point/position for several parameters at a time instant, or as a timeseries, or as a vertical profile for a time instant.
- **2 - Area**:  Retrieve data within a polygon or rectangular tile/subset at a time instant, or as a timeseries, or as a vertical profile for a time instant.
- **3 - Trajectory and Corridor**: Retrieve data along a 2D, 3D or 4D trajectory or within a defined corridor around a trajectory.

These patterns would be accessed through endpoints like:

```
/collections/{collectionID}/{queryType}?
  coords={wkt-geometry}&
  parameter-name={parameter_1},{parameter_n}&
  datetime={RFC3339/ISO8601}&
  f={format}&
  {queryType-specific-parameter_n_}={queryType-specific-parameter_n_value}
```
There are also other variants of these query patterns to make the API easier and more convenient to use. These are:

- **4 - Radius**: Retrieve data within a specified horizontal radius of a point/position 

- **5 - Cube**: Retrieve data within a specified 2D, 3D, or 4D bounding box. [Note: Currently the bounding box is specified as a polygon.]

- **6 - Location** Retrieve data for point/position identified by a name rather than coordinates.

- **7 - Items** Retrieve a feature by identifier. The coordinates in the feature could be used to create an EDR query. The feature could also be a previously stored query. Compatible with OGC API - Features - Part 1: Core.

- **8 - Instance** This allows discrimination between different versions of a collection. [Note: This may become part of API - Common as hierarchical collections.]

### EDR API Vision

The Environmental Data Retrieval (EDR) API can be considered both a 'simple' API and a 'convenience' API. 

It is considered a 'simple' API because:
* From an implementation viewpoint, the specification encourages a 'core' plus 'plug-in' framework;
* It does not require much domain knowledge compared to other OGC WxS and API standards;
* It uses Key/Value pairs;
* The metadata is based on the data being queried and is not verbose;
* The queries are “fixed” and predefined in the OpenAPI definition;
* The specification encourages the data publisher to publish data in fixed formats that are described within the metadata in a simple way.

It is considered a 'convenience' API because:
* It complements and provides synergy with other OGC APIs;
* The query patterns allow users to get just the data that they need;
* Users do not need to know the structure of the underlying data;
* It is not constrained to a particular data structure susch as grids, point clouds, features, etc.;
* It hides the complication of any underlying time structures because queries retrieve data for the time(s) that the user selects;
* It is the responsibility of the publisher to simplify appropriately the output, making it convenient for the user to consume the data;
* Implementations are constrained by the API definition, so all implementations will have the same URL structure.

The EDR API can be considered a 'Sampling API'. EDR queries create discrete sampling geometries that can sample a relatively persistent spatio-temporal data store resource. The query and its response are transient resources, which can be made persistent for re-use if required. EDR is agnostic as to whether the data store is a digital data cube that could be sampled anywhere or pre-existing samples of, or a model of, real world phenomena. While the former is the emphasis, EDR APIs can provide a list of pre-defined or pre-existing monitoring/modeled "locations" which can be accessed by location identifier. There is an assumption that the spatio-temporal data store is non-sparse, in that most queries are expected to return useful values rather than 'data not found'.

## Progress

### Draft Spec

The latest draft of the standard in this repository is built daily (based on the configuration contained in the [asciidoctor.json](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/asciidoctor.json) file):

* [OGC API - Environmental Data Retrieval Standard](http://docs.opengeospatial.org/DRAFTS/19-086.html)
* DRAFT [EDR OpenAPI Document](https://opengeospatial.github.io/ogcapi-environmental-data-retrieval/docs/edr_api.html)

### Implementations

Implementations are being advertised [here](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/Implementations.md). Some are live demos with real data, designed for a production environment, others are "work in progress" and some just "proofs of concept".

### Future Work

Proposed changes and extensions to the standard will be documented in the folder [proposals](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/tree/master/proposals).

Longer term work is being recorded [here](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Future-Work)

**Conformance Test Suite** work is starting at the beginning of 2021.

### EDR API Standard Working Group

The repository contains:
  
- [Working Group Charter](./EnvironmentalDataRetrievalAPI-SWG-Charter.adoc)
- [Standard document, as a work-in-progress draft](./standard_template/standard).

The charter lists initial deliverables in [section 4.1](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables) and a number of additional tasks in [section 4.2](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables). There is also an "out of scope" statement in [section 3.2](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#32-what-is-out-of-scope).

The repository also contains the plan of work and links to other relevant documents such as [minutes, actions and notes](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki#meetings) of meetings on the associated Wiki pages. 

**The public comment period on the EDR API closed 28th September 2020.** [Go here for more information.](https://www.ogc.org/standards/requests/215)

**A public Hackathon/Sprint** was held [virtually in March 2020](https://github.com/opengeospatial/EDR-API-Sprint) and another was held [9-10 November 2020](https://github.com/opengeospatial/OGCAPI-EDR-Sprint2) to help finalise the specification. There was a **public Webinar** outlining the Sprint's objectives on Wednesday 4 November 2020.

In December 2020, the OGC Technical Committee agreed, with no objections to unanimous consent, to have an **electronic vote** to recommend the specification for public release as an OGC Standard. 

### Best Practice

* [OGC API - Environmental Data Retrieval Best Practice](http://docs.opengeospatial.org/DRAFTS/20-065.html) - No Content yet

### Contributing

The contributor understands that any contributions, if accepted by the OGC Membership, shall be incorporated into OGC standards documents and that all copyright and intellectual property shall be vested to the OGC.

Pull Requests from contributors are welcomed. However, please note that by sending a Pull Request or Commit to this GitHub repository, you are agreeing to the terms in the Observer Agreement https://portal.ogc.org/files/?artifact_id=92169
