# OGC API - Environmental Data Retrieval

[<img src="http://www.opengeospatial.org/pub/www/files/OGC_Logo_2D_Blue_x_0_0.png" width="200"/>](https://www.opengeospatial.org)

This is the GitHub repository of the [OGC Environmental Data Retrieval API Standard Working Group (EDR API SWG)](https://www.opengeospatial.org/projects/groups/edr-apiswg).

The **[OGC API - Environmental Data Retrieval](https://ogcapi.ogc.org/edr/)** standard is part of the OGC API suite of standards. [OGC API standards](https://ogcapi.ogc.org) define modular API building blocks to spatially enable Web APIs in a consistent way. [OpenAPI](http://openapis.org) is used to define the reusable API building blocks.

### EDR API Collections
As with other OGC APIs that include a `/collections` end point, EDR supports distribution of _collections_ of geospatial data in particular ways. An EDR collection can contain virtually any data about the natural or built environment that needs to be _sampled_ using a spatio-temporal query pattern. The following is a list of examples that illustrate what this environmental data sampling paradigm might entail.

1. A climate model or weather reanalysis might be accessed at a point or within a bounding rectangle.
1. Geospatial gridded data such as a digital elevation model might be accessed along a transect.
1. Weather information from meteorological stations might be queried within a specified polygon.
1. An ensemble of forecast model data might be accessed for a specific location.
1. Information from a hydrologic sensor might be found spatially or accessed by ID.

EDR aims to specify the minimum yet sufficient diversity in metadata, query patterns, and response formats to enable this wide range of environmental data retrieval applications.

### EDR API Query Patterns
The EDR API allows a query, constructed of a spatio-temporal pattern, to retrieve data just for that pattern, from a data collection resource. Each of these patterns is optional, but a compliant API should implement at least one of them.

The main patterns are:
- **1 - Position**: Retrieve data for point/position for several parameters at a time instant, or as a timeseries, or as a vertical profile for a time instant.
- **2 - Area**:  Retrieve data within a polygon or rectangular tile/subset at a time instant, or as a timeseries, or as a vertical profile for a time instant.
- **3 - Trajectory and Corridor**: Retrieve data along a 2D, 3D or 4D trajectory or within a defined corridor around a trajectory.

These patterns would be accessed through endpoints like:

```
/collections/{collectionId}/{queryType}?
  coords={wkt-geometry}&
  parameter-name={parameter_1},{parameter_n}&
  datetime={RFC3339/ISO8601}&
  f={format}&
  {queryType-specific-parameter_n_}={queryType-specific-parameter_n_value}
```
There are also other variants of these query patterns to make the API easier and more convenient to use. These are:

- **4 - Radius**: Retrieve data within a specified horizontal radius of a point/position

- **5 - Cube**: Retrieve data within a specified 2D, 3D, or 4D bounding box. This is just a restricted special case of a polygon.

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
* It complements and provides synergy with other web based OGC APIs;
* The query patterns allow users to get just the data that they need;
* Users do not need to know the structure of the underlying data;
* It is not constrained to a particular data structure susch as grids, point clouds, features, etc.;
* It hides the complication of any underlying time structures because queries retrieve data for the time(s) that the user selects;
* It is the responsibility of the publisher to simplify appropriately the output, making it convenient for the user to consume the data;
* Implementations are constrained by the API definition, so all implementations will have the same URL structure.

The EDR API can be considered a 'Sampling API'. EDR queries create discrete sampling geometries that can sample a relatively persistent spatio-temporal data store resource. The query and its response are transient resources, which can be made persistent for re-use if required. EDR is agnostic as to whether the data store is a digital data cube that could be sampled anywhere or pre-existing samples of, or a model of, real world phenomena. While the former is the emphasis, EDR APIs can also provide a list of pre-defined or pre-existing monitoring/modeled "locations" which can be accessed by location identifier. There is an assumption that the spatio-temporal data store is non-sparse, in that most queries are expected to return useful values rather than 'data not found'.

## Progress

### Standard and Draft Specifications

The standard is in the V1.1 Branch.

The Master Branch is the latest draft of the standard, currently V1.2.0, and is built daily (based on the configuration contained in this [GitHub Action](https://github.com/opengeospatial/ogcna-auto-review/blob/main/.github/workflows/generate_19-086r6.yml) file):

* [OGC API - Environmental Data Retrieval Standard, Version 1.0.0](https://docs.ogc.org/is/19-086r4/19-086r4.html)
* [OGC API - Environmental Data Retrieval Standard, with Corrigendum, Version 1.0.1](https://docs.ogc.org/is/19-086r5/19-086r5.html)
* [OGC API - Environmental Data Retrieval Standard, Version 1.1.0](https://opengeospatial.github.io/ogcna-auto-review/19-086r6.html)
* DRAFT [EDR OpenAPI Document](https://opengeospatial.github.io/ogcapi-environmental-data-retrieval/docs/edr_api.html)

Version 1.2 will be re-labelled as OGC API - Environmental Data Retrieval, Part 1: Core.

A Part 2: Publish-Subscribe is being developed using AsyncAPI as well as OpenAPI to support an asynchronous "publish and subscribe" model for data and notifications. The intent is that will also be applicable to, and usable by, other OGC APIs:
* DRAFT [OGC API-Environmental Data Retrieval Standard, Part 2: Publish-Subscribe](https://docs.ogc.org/DRAFTS/23-057.html)

### Conformance Test Suite

An OGC API-EDR conformance test suite has been developed so that implementations can be formally certified as conforming to the standard, if so desired.
 
The [Executable Test Suite (ETS) of OGC API - EDR](https://cite.ogc.org/teamengine/) is available on the OGC Validator.

Implementations that pass the conformance tests can be submitted for Compliance certification, by following the steps to [Get Certified](https://www.ogc.org/compliance/getCertified).

Implementations that are Certified OGC Compliant are listed on the [OGC Product Database](https://www.ogc.org/resource/products/compliant?display_opt=1&specid=1247).

If you encounter any bugs, please [log the issues](https://github.com/opengeospatial/ets-ogcapi-edr10/issues).

There are three approaches to testing:

* Option 1: Run the ETS on the [OGC Validator](https://cite.ogc.org/teamengine/).

* Option 2: Run the ETS through `docker` by executing this command: `docker run -p 8081:8080 ogccite/ets-ogcapi-edr10`

* Option 3: Use the ETS from within an IDE such as Eclipse or IntelliJ. There is a [Maven project](https://github.com/opengeospatial/ets-ogcapi-edr10). If you are planning to use an IDE for testing, we can arrange a brief telecon to help you set up your environment.

### Implementations

Implementations are being advertised [here](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/deployments.md). Some are live demos with real data, designed for a production environment, others are "work in progress" and some just "proofs of concept". There are other implementations in development but not yet public.

### Development Guidelines

The development of the API has used other [well-established standards and guidelines](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Guidelines). The overlaps, and gaps, with other OGC standards are also being described [here](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Examples).  The API also supports the [OGC Web API Guidelines](ogc-web-api-guidelines-checklist.md).

### Future Work

Proposed changes and extensions to the standard will be documented in the folder [proposals](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/tree/master/proposals).

Longer term work is being recorded [here](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Future-Work)

**Conformance Test Suite** work started at the beginning of 2021 using [TeamEngine](https://github.com/opengeospatial/teamengine).

### EDR API Standard Working Group

The repository contains:

- [Working Group Charter](./EnvironmentalDataRetrievalAPI-SWG-Charter.adoc)
- [Standard document, as a work-in-progress draft](./standard_template/standard).

The charter lists initial deliverables in [section 4.1](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables) and a number of additional tasks in [section 4.2](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables). There is also an "out of scope" statement in [section 3.2](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#32-what-is-out-of-scope).

The repository also contains the plan of work and links to other relevant documents such as [minutes, actions and notes](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki#meetings) of meetings on the associated Wiki pages.

**The public comment period on the EDR API closed 28th September 2020.** [Go here for more information.](https://www.ogc.org/standards/requests/215)

**A public Hackathon/Sprint** was held [virtually in March 2020](https://github.com/opengeospatial/EDR-API-Sprint) and another was held [9-10 November 2020](https://github.com/opengeospatial/OGCAPI-EDR-Sprint2) to help finalise the specification. There was a **public Webinar** outlining the Sprint's objectives on Wednesday 4 November 2020.

In December 2020, the OGC Technical Committee agreed, with no objections to unanimous consent, to have an electronic vote to recommend the specification for public release as an OGC Standard. The OGC TC e-vote was **passed** with quorum on 8 March 2021. The OGC Planning Committee on 30 March 2021 voted, with no objections to unanimous consent, **to recommend the OGC API - EDR as a full OGC Standard**, and to not change the name.

On 28 April 2021, at 16:00 UTC, the standard started editing for publication as a formal standard.

The [OGC API - EDR standard](https://www.ogc.org/standards/ogcapi-edr) was formally published on 13 September 2021 and a Corrigendum V1.0.1 published on 5 August 2022.

The Working Group is now developing a backwards-compatible V1.1 and future enhancements.

### Best Practice

* [OGC API - Environmental Data Retrieval Best Practice](http://docs.opengeospatial.org/DRAFTS/20-065.html) - No Content yet

### Contributing

The contributor understands that any contributions, if accepted by the OGC Membership, shall be incorporated into OGC standards documents and that all copyright and intellectual property shall be vested to the OGC.

Pull Requests from contributors are welcomed. However, please note that by sending a Pull Request or Commit to this GitHub repository, you are agreeing to the terms in the Observer Agreement https://portal.ogc.org/files/?artifact_id=92169
