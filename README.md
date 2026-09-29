# OGC API - Environmental Data Retrieval

[<img src="https://www.ogc.org/pub/www/files/OGC_Logo_2D_Blue_x_0_0.png" width="200"/>](https://www.ogc.org/)

The **[OGC API - Environmental Data Retrieval (EDR)](https://ogcapi.ogc.org/edr/)** standards define lightweight query interfaces for retrieving spatio-temporal data. A client requests data at a position, within an area, along a trajectory, and so on, and gets back only the data for that query.

EDR is part of the [OGC API](https://ogcapi.ogc.org) family of standards, which define modular API building blocks to spatially enable Web APIs in a consistent way. The building blocks are defined using [OpenAPI](https://www.openapis.org/).

This repository is where the [OGC](https://www.ogc.org/) EDR API Standards Working Group (SWG) develops and maintains the EDR standards.

## Standards at a glance

| Part | Latest version | Status | OGC doc | Read |
|---|---|---|---|---|
| [Part 1: Core](#part-1-core) | 1.2 | Approved standard, published 2026-09-08 | 19-086r9 | [HTML](https://docs.ogc.org/is/19-086r9/19-086r9.html) · [PDF](https://docs.ogc.org/is/19-086r9/19-086r9.pdf) |
| [Part 2: Publish-Subscribe Workflow](#part-2-publish-subscribe-workflow) | 1.0 | Approved standard, published 2024-09-23 | 23-057r1 | [HTML](https://docs.ogc.org/is/23-057r1/23-057r1.html) · [PDF](https://docs.ogc.org/is/23-057r1/23-057r1.pdf) |
| [Part 3: Service Profiles](#part-3-service-profiles) | 1.0 (draft) | Public comment open until 2026-10-21 | 25-014r1 | [Draft for comment](https://files.ogc.org/file/klygae855164e973f4d84a9d343dbb737a230) |

All published EDR documents are also listed on the [OGC API - EDR standard page](https://www.ogc.org/standards/ogcapi-edr/).

## Part 1: Core

Part 1 defines the core EDR API: how a server describes its data collections, and the query patterns clients use to retrieve data from them (see [Query patterns](#query-patterns)). Versions up to and including 1.2 are published as *OGC API - Environmental Data Retrieval Standard*. The name "Part 1: Core" is used to distinguish it from Parts 2 and 3.

**Published versions**

| Version | OGC doc | Published | Read |
|---|---|---|---|
| 1.2 (current) | 19-086r9 | 2026-09-08 | [HTML](https://docs.ogc.org/is/19-086r9/19-086r9.html) · [PDF](https://docs.ogc.org/is/19-086r9/19-086r9.pdf) |
| 1.1 | 19-086r6 | 2023-07-27 | [HTML](https://docs.ogc.org/is/19-086r6/19-086r6.html) · [PDF](https://docs.ogc.org/is/19-086r6/19-086r6.pdf) |
| 1.0.1 (corrigendum) | 19-086r5 | 2022-08-05 | [HTML](https://docs.ogc.org/is/19-086r5/19-086r5.html) · [PDF](https://docs.ogc.org/is/19-086r5/19-086r5.pdf) |
| 1.0 | 19-086r4 | 2021-08-13 | [HTML](https://docs.ogc.org/is/19-086r4/19-086r4.html) · [PDF](https://docs.ogc.org/is/19-086r4/19-086r4.pdf) |

Version 1.2 is backwards compatible with 1.1.

**Corrigenda in preparation:** some minor errors found in 1.0.1 and 1.1 were fixed in 1.2. For deployments that are not yet ready to move to 1.2, the fixes are being published as corrigenda 1.0.2 (19-086r7, branch [`1.0.2`](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/tree/1.0.2)) and 1.1.1 (19-086r8, branch [`1.1.1`](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/tree/1.1.1)).

**OpenAPI definitions:** the source YAML is in [`core/standard/openapi/`](core/standard/openapi/). Bundled single-file versions for [OpenAPI 3.0](ogcapi-environmental-data-retrieval-1-oas30.bundled.json) and [OpenAPI 3.1](ogcapi-environmental-data-retrieval-1-oas31.bundled.json) are generated automatically in the repository root, and the 3.1 bundle can be browsed in the [interactive API viewer](https://opengeospatial.github.io/ogcapi-environmental-data-retrieval/docs/edr_api.html). Official schemas for published versions are on [schemas.opengis.net](https://schemas.opengis.net/ogcapi/edr/).

## Part 2: Publish-Subscribe Workflow

Part 2 adds an asynchronous "publish and subscribe" model for data and notifications, using [AsyncAPI](https://www.asyncapi.com/) alongside OpenAPI. It is intended to be usable by other OGC APIs as well.

Version 1.0 (23-057r1) was published on 2024-09-23 and is available in [HTML](https://docs.ogc.org/is/23-057r1/23-057r1.html) and [PDF](https://docs.ogc.org/is/23-057r1/23-057r1.pdf). Source: [`extensions/pubsub/standard/`](extensions/pubsub/standard/).

## Part 3: Service Profiles

Part 1 was designed to be flexible and easy for Web developers to implement. As it has been widely adopted, some communities have asked to restrict that flexibility so that servers and clients within their domain work together more reliably. A set of such stricter rules for a particular community is a *profile*.

Part 3 defines how to specify a profile of Part 1. It covers restrictive profiles only, and the restrictions are expressed as JSON Schema fragments that can be tested formally. Like Part 2, it is intended to be usable by other OGC APIs.

**Public comment is open from 2026-09-21 until 2026-10-21.** Read the [draft for public comment](https://files.ogc.org/file/klygae855164e973f4d84a9d343dbb737a230) and submit comments as [GitHub issues](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/issues). See the [OGC announcement](https://www.ogc.org/requests/ogc-api-edr-part-3-service-profiles-public-comment/) for details.

The latest editor's draft is built from [`extensions/service_profiles/standard/`](extensions/service_profiles/standard/) and published in [HTML](https://opengeospatial.github.io/ogcapi-environmental-data-retrieval/extensions/service_profiles/standard/25-014.html).

## About EDR

### Collections

As with other OGC APIs that have a `/collections` endpoint, EDR serves *collections* of geospatial data. An EDR collection can hold almost any data about the natural or built environment that is best *sampled* with a spatio-temporal query. For example:

1. A climate model or weather re-analysis accessed at a point or within a bounding rectangle.
1. Gridded data such as a digital elevation model accessed along a transect.
1. Observations from weather stations queried within a polygon.
1. An ensemble of forecast model data accessed for a named location.
1. Readings from a hydrologic sensor found spatially or accessed by identifier.

EDR aims to specify the minimum, yet sufficient, variety of metadata, query patterns and response formats to support this range of uses. Any collection of data with consistent spatio-temporal coordinates can be served, not only environmental data.

### Query patterns

Each query pattern is optional, but an EDR API should implement at least one. Queries are made against a collection:

```
/collections/{collectionId}/{queryType}?
  coords={wkt-geometry}&
  parameter-name={parameter_1},{parameter_n}&
  datetime={RFC3339/ISO8601}&
  f={format}&
  {queryType-specific-parameter}={value}
```

| Query type | Retrieves data… |
|---|---|
| `position` | at a point, for a time instant, as a time series, or as a vertical profile |
| `radius` | within a horizontal radius of a point |
| `area` | within a polygon |
| `cube` | within a 2D, 3D or 4D bounding box (a restricted case of `area`) |
| `trajectory` | along a 2D, 3D or 4D path |
| `corridor` | within a corridor around a trajectory |
| `locations` | at a location identified by name rather than coordinates |
| `items` | as features, by identifier; compatible with OGC API - Features - Part 1: Core. A feature can hold coordinates for a new EDR query, or be a stored query. |
| `instances` | from a specific version (instance) of a collection. All other query types can be used under `/collections/{collectionId}/instances/{instanceId}/`. |

<details>
<summary><strong>Design goals</strong></summary>

EDR can be considered both a "simple" API and a "convenience" API.

It is a *simple* API because:

* From an implementation viewpoint, the specification encourages a "core" plus "plug-in" framework;
* It does not require much domain knowledge compared to other OGC WxS and API standards;
* It uses key/value pairs;
* The metadata is based on the data being queried and is not verbose;
* The queries are fixed and predefined in the OpenAPI definition;
* The specification encourages the data publisher to publish data in fixed formats that are described within the metadata in a simple way.

It is a *convenience* API because:

* It complements, and works alongside, other Web-based OGC APIs;
* The query patterns allow users to get just the data they need;
* Users do not need to know the structure of the underlying data;
* It is not constrained to a particular data structure such as grids, point clouds or features;
* It hides the complexity of any underlying time structures, because queries retrieve data for the time(s) the user selects;
* It is the publisher's responsibility to simplify the output appropriately, making it convenient for the user to consume;
* Implementations are constrained by the API definition, so all implementations have the same URL structure.

EDR can also be considered a *sampling* API. EDR queries create discrete sampling geometries that sample a relatively persistent spatio-temporal data store. The query and its response are transient resources, which can be made persistent for re-use if required. EDR is agnostic as to whether the data store is a data cube that can be sampled anywhere, or a set of pre-existing samples or models of real-world phenomena. While the former is the emphasis, EDR APIs can also offer a list of pre-defined monitoring or modelled locations that can be accessed by identifier. EDR assumes the data store is non-sparse, so that most queries return useful values rather than "data not found".

</details>

## Implementations

Server and client implementations are listed in [`implementations/`](implementations/README.adoc). Pull requests adding new implementations are welcome.

[`deployments.md`](deployments.md) is an older list of demonstration servers, many of them from the development of version 1.0.

## Conformance testing

An Executable Test Suite (ETS) lets implementations be tested, and optionally certified, as conforming to the standard. The current ETS covers versions 1.0 and 1.0.1 of Part 1. There are three ways to run it:

1. On the [OGC Validator](https://cite.ogc.org/teamengine/).
1. With Docker: `docker run -p 8081:8080 ogccite/ets-ogcapi-edr10`
1. From an IDE such as Eclipse or IntelliJ, using the [Maven project](https://github.com/opengeospatial/ets-ogcapi-edr10).

Please report problems with the test suite in its [issue tracker](https://github.com/opengeospatial/ets-ogcapi-edr10/issues).

Implementations that pass can be submitted for certification through the [OGC Compliance Program](https://www.ogc.org/how-our-compliance-program-works/). Certified products are listed in the [OGC product database](https://portal.ogc.org/public_ogc/compliance/compliant.php?display_opt=1&specid=1247).

## Repository guide

**Branches**

| Branch | Contents |
|---|---|
| `master` | Part 1 at the latest version (currently 1.2), plus the Part 2 and Part 3 sources. Future work happens here. |
| `1.0.1`, `1.1.0` | Sources of the published 1.0.1 and 1.1 versions of Part 1 |
| `1.0.2`, `1.1.1` | Corrigenda to 1.0.1 and 1.1 in preparation |

**Directories**

| Path | Contents |
|---|---|
| [`core/standard/`](core/standard/) | Part 1 source (Metanorma AsciiDoc) and OpenAPI definitions |
| [`extensions/pubsub/standard/`](extensions/pubsub/standard/) | Part 2 source |
| [`extensions/service_profiles/standard/`](extensions/service_profiles/standard/) | Part 3 source |
| `*.bundled.json` (root) | Generated OpenAPI bundles. Do not edit by hand. |
| [`implementations/`](implementations/) | Server and client implementations |
| [`ogc-web-api-guidelines/`](ogc-web-api-guidelines/) | [OGC Web API Guidelines](https://github.com/opengeospatial/ogc-web-api-guidelines) checklists for each version and part |
| [`use-cases/`](use-cases/) | Use cases that informed the standard |
| [`proposals/`](proposals/) | Process for proposing new features |
| [`docs/`](docs/) | SWG charter, development process notes and background material |

**Building the documents:** each standard directory has a `Makefile` that builds HTML and PDF with [Metanorma](https://www.metanorma.org/). Run `make all` in that directory, or `METANORMA_DOCKER=metanorma/mn make all` to use Docker instead of a local install. See [`core/standard/README.adoc`](core/standard/README.adoc) for details.

## Getting involved

* Report problems or suggest changes through [GitHub issues](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/issues). Change requests for published standards can also be submitted through the [OGC change request form](https://portal.ogc.org/public_ogc/change_request.php).
* Meeting [minutes, actions and notes](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki#meetings) are on the wiki, along with the [development guidelines](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Guidelines), [comparisons with other OGC standards](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Examples) and [longer-term future work](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/wiki/Future-Work).
* The SWG's scope and deliverables are set out in its [charter](docs/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc). OGC members can join through the [OGC Standards Working Groups](https://www.ogc.org/standards/technical-committee/standards-working-groups/) page.
* To report a security vulnerability, see [SECURITY.md](SECURITY.md).

## History

| Date | Milestone |
|---|---|
| March 2020 | [First virtual sprint](https://github.com/opengeospatial/EDR-API-Sprint) |
| September 2020 | Public comment period on version 1.0 closed (28 September) |
| November 2020 | [Second sprint](https://github.com/opengeospatial/OGCAPI-EDR-Sprint2) (9–10 November) |
| 2021-08-13 | Version 1.0 published (19-086r4) |
| 2022-08-05 | Corrigendum 1.0.1 published (19-086r5) |
| 2023-07-27 | Version 1.1 published (19-086r6) |
| 2024-09-23 | Part 2: Publish-Subscribe Workflow 1.0 published (23-057r1) |
| 2026-09-08 | Version 1.2 published (19-086r9) |
| 2026-09-21 | Part 3: Service Profiles released for public comment |

## Contributing

The contributor understands that any contributions, if accepted by the OGC Membership, shall be incorporated into OGC standards documents and that all copyright and intellectual property shall be vested to the OGC.

Pull Requests from contributors are welcomed. However, please note that by sending a Pull Request or Commit to this GitHub repository, you are agreeing to the terms in the Observer Agreement https://portal.ogc.org/files/?artifact_id=92169
