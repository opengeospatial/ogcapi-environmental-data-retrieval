# Specification for the Environmental Data Retrieval API

This specification for the Environmental-Data-Retrieval API (EDR API) is based on some key principles:

### A Collection

The definition of a `Collection` is very basic. All data parameters in a collection `MUST` follow these rules:

1. Share the same Geo-Temporal dimensions and units of measurement.
2. Can all be re-gridded or interpolated to any of the output CRS values advertised by the `Collection`
3. Can all be transformed into the output formats advertised by the `Collection`

### The API is completely data source agnostic

With this approach, each `Collection` is treated as a `black box` with a defined set of interfaces, regardless of the underlying structure of the data. It is the data publisher's responsibility to make the `Collection` conform to the API contract.  This means that a `Collection` could be a dynamically generated set of values or a query on a physical data source, as long as the interface to the `Collection` conforms with the defined API contracts. 

### A family of simple APIs each with a limited set of functionality

Even if not all of the information available in the underlying source is accessible, interoperability should be more straightforward, as each member of the API family has a constrained set of rules to obey.  Implementation should also be easier, as each query type can be optimised as a bespoke algorithm (with different technology if required) rather than having to cope with a rich filter-based input which has to be parsed before the query is made. 

### Each API should be self-describing

An API consumer should only have to supply the Spatial and Temporal values (and even then the API will supply the bounds of the data collection), the APIs should not expect any specialist knowledge beyond that required for software development. This approach depends on several factors. Firstly the APIs need to be simple enough that they can be described by standard API documentation tooling. Secondly the data publisher needs to transform the information that the API provides access to into an easily understandable set of data values. Finally there needs to be a mechanism to provide access to detailed metadata, for those that need it, to describe the data without swamping the returned data values with metadata information.  This specification proposes using metadata registries to allow API consumers to discover more information if they require it.

### Collections can have multiple instances or versions

A common requirement in the scientific domain is to be able to publish updated versions of information. Whilst this could be handled by exposing the new versions of the data source as a different `Collection`, this specification proposes a more structured approach by adding the concept of `Instances` of a `Collection`.  This would remove the need for a best practice naming convention and, following the argument in the previous section, make it much easier for API consumers to understand that the data is just another version of an existing collection.

### A Collection does not need to support all the members in the API family to be compliant with the standard

Data providers should only have to implement those APIs that are applicable to the data that they are publishing.





