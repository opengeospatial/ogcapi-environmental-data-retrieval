# OGC EDR API Support of OGC Web API Guidelines

# Overview

This document outlines EDR API support of the design principles of the [OGC Web API Guidelines](https://github.com/opengeospatial/OGC-Web-API-Guidelines).

- [x]  Principle #1 – Don’t Reinvent
  - adopts concepts from OGC API - Common (landing page, conformance, collections, datetime query parameter) and OGC API - Features (`/collections/{collectionId}/items`) and uses WKT and ISO8601 for most syntax
- [x]  Principle #2 – Keep the API Simple and Intuitive
  - allows for minimal compliant implementation (1 query type)
  - provides interaction with minimal domain knowledge
  - provide query types as convenience / shortcuts to common subsetting patterns
- [x]  Principle #3 - Use Well-Known Resource Types
  - provides a resource agnostic and inclusive API
  - CoverageJSON resource type is `application/vnd.cov+json`. Another type may be registered with IANA if appropriate
- [x]  Principle #4 – Construct consistent URIs
  - adopts collection of resources principle
    - `/collections/{collectionId}/items`
    - `/collections/{collectionId}/{queryType}`
- [x]  Principle #5 – Use HTTP Methods consistent with RFC 7231
  - implements resource-based HTTP `GET` methods
  - future work may add support for HTTP `POST` 
     - to help with URL truncation
     - to help with security of sending sensitive data
  - future work may add support for HTTP `OPTIONS`, required for CORS/preflight
- [x]  Principle #6 – Put Selection Criteria behind the ‘?’
  - provides query parameter support in order to further subset a given resource/query type
- [x]  Principle #7 – Error Handling and use of HTTP Status Codes
  - provides exception schema (code and description) as well as the appropriate HTTP status codes
- [x]  Principle #8 – Use explicit list of HTTP Status Codes
  - 200, 202, 204, 304, 308, 400, 401, 403, 404, 405, 406, 413, 500 (see Table 6)
- [x]  Principle #9 – Use of HTTP Header
  - allows for Link headers
- [ ]  Principle #10 - Allow flexible Content Negotiation
  - currently not addressed
- [ ]  Principle #11 - Pagination
  - eliminates pagination given the design patterns of the query types to provide succinct results from discrete sampling
- [ ]  Principle #12 – Processing Resources
  - Not applicable
- [x]  Principle #13 – Support Metadata
  - provides `service-desc` and `service-doc` link relations
  - provides metadata via extended collections model
- [x]  Principle #14 – Consider your Security needs
  - supports HTTPS (See 6.6) and RFC2818
  - it is recommended to explicitly NOT support HTTP, addressing
       - privacy issues
       - insecure communication
  - it is recommended that HTTP `POST` is used as an additional security mechanism
- [x]  Principle #15 – API Description
  - supports OpenAPI for API documentation
- [x]  Principle #16 - Use well-known identifiers
  - provides media types and link relations that are based on IANA and extended per the OGC Definitions Server
- [x]  Principle #17 - Use explicit relations
  - The primary function is query and a single response. Links to associated resources describing the query response are explicit (have we got there yet?)
- [x]  Principle #18 - Support W3C Cross-Origin Resource Sharing
  - CORS is supported (See 10.4)
- [x]  Principle #19 - Resource encodings
  - supports JSON, GeoJSON, HTML and CoverageJSON
- [x]  Principle #20 - Good APIs are testable from the beginning
  - demonstrates this via the EDR ETS
  - enables standard programming libraries in implementing standard HTTP request/response, headers and well-known media types and design patterns
- [x]  Principle #21 - Specify whether operations are safe and/or idempotent
  - provides both safe and idempotent operations via HTTP `GET`
- [x]  Principle #22 – Make resources discoverable
  - implements common OGC API link relations
- [x]  Principle #23 - Make default behavior explicit
  - collection metadata provides the ability for link relations via URL templates along with explanations of templated variables
  - example: https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/candidate-standard/examples/collections_metadata_JSON_1.adoc
