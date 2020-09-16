# Candidate specification for the Environmental Data Retrieval API

This is the GitHub repository of the [OGC Environmental Data Retrieval API Standard Working Group (EDR API SWG)](https://www.opengeospatial.org/projects/groups/edr-apiswg).

**EDR public comment period is open and closes September 28th.** [Go here for more information.](https://www.ogc.org/standards/requests/215)

The **OGC API - Environmental Data Retrieval** candidate standard is part of the OGC API suite of standards. [OGC API standards](https://ogcapi.ogc.org) define modular API building blocks to spatially enable Web APIs in a consistent way. [OpenAPI](http://openapis.org) is used to define the reusable API building blocks.

The repository contains:
  
- [Working Group Charter](./EnvironmentalDataRetrievalAPI-SWG-Charter.adoc)
- [Standard document, as a work-in-progress draft](./standard_template/standard). 
- [Best Practice document, as a work-in-progress draft](./BestPractice.md)

It will also contain the plan of work and links to other relevant documents such as [minutes, actions and notes](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/wiki#meetings) of meetings on the associated Wiki pages. 

## Draft Spec

The latest draft of the standard in this repository is built daily (based on the configuration contained in the [asciidoctor.json](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/asciidoctor.json) file):

* [OGC API - Environmental Data Retrieval Standard](http://docs.opengeospatial.org/DRAFTS/19-086.html)
* DRAFT [EDR OpenAPI Document](https://opengeospatial.github.io/Environmental-Data-Retrieval-API/docs/edr_api.html)

### Best Practice

* [OGC API - Environmental Data Retrieval Best Practice](http://docs.opengeospatial.org/DRAFTS/20-065.html)

## EDR API Vision

The EDR API can be considered a 'Sampling API'. EDR queries create discrete sampling geometries that can sample a relatively persistent data store resource. The query and its response are transient resources, which can be made persistent for re-use if required. EDR is agnostic to whether the data store is a digital data cube that could be sampled anywhere or pre-existing samples of, or a model of, real world phenomena. While the former is the emphasis, EDR APIs can provide a list of pre-defined or pre-existing monitoring/modeled "locations" which can be accessed by location identifier. There is an assumption that the data store is non-sparse, in that most queries are expected to return useful values rather than 'data not found'.

### EDR API Query Patterns
The EDR API Standard Working Group charter lists initial deliverables in [section 4.1](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables) and a number of additional tasks in [section 4.2](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables). There is also an "out of scope" statement in [section 3.2](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#32-what-is-out-of-scope).

Summarizing these sections. EDR Query Patterns will be:  
- **1 - Position**: Retrieve data for point/position or identified location with n parameters at a time instant, or a timeseries, or a vertical profile for a time instant.
- **2 - Area**:  Retrieve data within a polygon or rectangular tile/subset at a time instant, or a timeseries, or a vertical profile for a time instant.
- **3 - Trajectory and Corridor**: Retrieve data along a 2D, 3D or4D trajectory or within a defined corridor around a trajectory.

- **4 - Ensembles**: Support for explicitly related ensembles of EDR resources.[Note: This will be in a later version]

These patterns would be accessed through endpoints like:

```
/collections/{collectionID}/{queryType}?
  coords={wkt-geometry}&
  parametername={parameter_1},{parameter_n}&
  datetime={RFC3339/ISO8601}&
  outputformat={format}&
  {queryType-specific-parameter_n_}={queryType-specific-paramete_n_value}
```


## [Contributing](CONTRIBUTING.md)

The contributor understands that any contributions, if accepted by the OGC Membership, shall be incorporated into OGC standards documents and that all copyright and intellectual property shall be vested to the OGC.

Pull Requests from contributors are welcomed. However, please note that by sending a Pull Request or Commit to this GitHub repository, you are agreeing to the terms in the Observer Agreement https://portal.ogc.org/files/?artifact_id=92169
