## OGC API - Environmental Data Retrieval Version 1.0

To comply with [Policy Directive 50](https://portal.ogc.org/public_ogc/directives/directives.php#50), the following should be completed.

See an example in the [OGC API - Common - Part 1: Core Standard](https://docs.ogc.org/is/19-072/19-072.html#_c483b499-4a80-4d7d-997e-100e0d89a0b3).

| # | Principle | Discussion
| -- | -- | --
|	1	|	Don’t reinvent	|	adopts concepts from OGC API - Common (landing page, conformance, collections, datetime query parameter) and OGC API - Features (`/collections/{collectionId}/items`) and uses WKT and ISO8601 for most syntax
|	2	|	Keep it simple and intuitive	| allows for minimal compliant implementation (1 query type) - provides interaction with minimal domain knowledge - provide query types as convenience / shortcuts to common subsetting patterns
|	3	|	Use well-known resource types	|	provides a resource agnostic and inclusive API - CoverageJSON resource type is `application/vnd.cov+json`. Another type may be registered with IANA if appropriate
|	4	|	Construct consistent URIs	|	adopts collection of resources principle  - `/collections/{collectionId}/items`  - `/collections/{collectionId}/{queryType}`
|	5	|	Use HTTP methods consistent with RFC 7231	| implements resource-based HTTP `GET` methods - future work may add support for HTTP `POST` - to help with URL truncation - to help with security of sending sensitive data  - future work may add support for HTTP `OPTIONS`, required for CORS/preflight
|	6	|	Put selection criteria behind the ‘?’	| provides query parameter support in order to further subset a given resource/query type
|	7	|	Error handling and use of HTTP status codes	| provides exception schema (code and description) as well as the appropriate HTTP status codes
|	8	|	Use explicit list of HTTP status codes	| 200, 202, 204, 304, 308, 400, 401, 403, 404, 405, 406, 413, 500 (see Table 6)
|	9	|	Use of HTTP header	| allows for Link headers
|	10	|	Allow flexible content negotiation	| currently not addressed
|	11	|	Pagination	| eliminates pagination given the design patterns of the query types to provide succinct results from discrete sampling
|	12	|	Processing resources	| Not applicable
|	13	|	Support metadata	| provides `service-desc` and `service-doc` link relations - provides metadata via extended collections model
|	14	|	Consider your security needs	| supports HTTPS (See 6.6) and RFC2818 - it is recommended to explicitly NOT support HTTP, addressing    - privacy issues  - insecure communication  - it is recommended that HTTP `POST` is used as an additional security mechanism
|	15	|	API description	| supports OpenAPI for API documentation
|	16	|	Use well-known identifiers	| provides media types and link relations that are based on IANA and extended per the OGC Definitions Server
|	17	|	Use explicit relations	| The primary function is query and a single response. Links to associated resources describing the query response are explicit (have we got there yet?)
|	18	|	Support W3C cross-origin resource sharing	| CORS is supported (See 10.4)
|	19	|	Resource encodings	| supports JSON, GeoJSON, HTML and CoverageJSON
|	20	|	Good APIs are testable from the beginning	| demonstrates this via the EDR ETS - enables standard programming libraries in implementing standard HTTP request/response, headers and well-known media types and design patterns
|	21	|	Specify whether operations are safe and/or idempotent	| provides both safe and idempotent operations via HTTP `GET`
|	22	|	Make resources discoverable	| implements common OGC API link relations
|	23	|	Make default behavior explicit	| collection metadata provides the ability for link relations via URL templates along with explanations of templated variables  - example: https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/candidate-standard/examples/collections_metadata_JSON_1.adoc
