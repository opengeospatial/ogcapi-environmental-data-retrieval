# Standard template

This folder contains the content for OGC API - Environmental Data Retrieval - Part 2: Publish-Subscribe workflow.


The repo is organized as follows:

* standard - the main standard document content
  - organized in multiple sections and directories
* openapi - normative OpenAPI components specified by the standard
* examples - JSON and XML examples

## Building

Build the document from this folder.

`docker run -v "$(pwd)":/metanorma -v ${HOME}/.fontist/fonts/:/config/fonts  metanorma/metanorma  metanorma compile --agree-to-terms -t ogc -x html standard/document.adoc`
