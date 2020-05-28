# Candidate specification for the Environmental-Data-Retrieval-API

[![Join the chat at https://gitter.im/opengeospatial/Environmental-Data-Retrieval-API](https://badges.gitter.im/opengeospatial/Environmental-Data-Retrieval-API.svg)](https://gitter.im/opengeospatial/Environmental-Data-Retrieval-API?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is the GitHub repository of the [OGC Environmental Data Retrieval API Standard Working Group (EDR-API SWG)](https://www.opengeospatial.org/projects/groups/edr-apiswg).

It contains:
  
- [Working Group Charter](./EnvironmentalDataRetrievalAPI-SWG-Charter.adoc)
- [Standard document, as a work-in-progress draft](./standard_template/standard). 

It will also contain the plan of work and links to other relevant documents such as [minutes, actions and notes](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/wiki#meetings) of meetings on the associated Wiki pages. 

## Draft Spec

The latest draft of the standard in this repository is built daily (based on the configuration contained in the [asciidoctor.json](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/asciidoctor.json) file):

* [OGC API - Environmental Data Retrieval Standard](http://docs.opengeospatial.org/DRAFTS/19-086.html)
* [DRAFT OpenAPI Document](https://opengeospatial.github.io/Environmental-Data-Retrieval-API/docs/edr_api.html)

## EDR Vision

The EDR API can be considered a 'Sampling API'. EDR queries create discrete sampling geometries that can sample a relatively persistent data store resource. The query and its response are transient resources, which can be made persistent for re-use if required. EDR is agnostic to whether the data store is a digital data cube that could be sampled anywhere or pre-existing samples of, or a model of, real world phenomena. While the former is the emphasis, EDR APIs can provide a list of pre-defined or pre-existing monitoring/modeled "locations" which can be accessed by location identifier.

### EDR Query Patterns
The EDR charter lists initial deliverables in [section 4.1](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables) and a number of additional tasks in [section 4.2](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#41-initial-deliverables). There is also an "out of scope" statement in [section 3.2](https://github.com/opengeospatial/Environmental-Data-Retrieval-API/blob/master/EnvironmentalDataRetrievalAPI-SWG-Charter.adoc#32-what-is-out-of-scope).

Summarizing these sections. EDR Query Patterns will be:  
- **1 - Core**: Point/position or identified location with n parameters at a time instant and/or a timeseries.
- **2 - Sampling Geometries**: Vertical profile for a time instant and rectangular or polygonal tile/subset.
- **3 - Trajectories and Corridors**: Samples along a 2D-4D trajectory or within a defined corridor.
- **4 - Ensembles**: Support for explicitly related ensembles of EDR resources.

These patterns would be accessed through endpoints like:

```
/collections/{collectionID}/{queryType}?
  coords={wkt-geometry}&
  parametername={parameter_1},{parameter_n}&
  datetime={RFC3339/ISO8601}&
  outputformat={format}&
  {queryType-specific-parameter_n_}={queryType-specific-paramete_n_value}
```
