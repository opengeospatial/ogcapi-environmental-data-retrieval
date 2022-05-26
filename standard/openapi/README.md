# OpenAPI definitions

This example API definition can be used to provide an OpenAPI 3.0 definition for an implementation of _OGC API - Environmental Data Retrieval_.
The API definition can be visualized with [SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/opengeospatial/ogcapi-environmental-data-retrieval/master/standard/openapi/ogcapi-environmental-data-retrieval-1.bundled.json).

The list of supported paths should be adjusted in `ogcapi-environmental-data-retrieval-1.yaml`.

# Building the OpenAPI bundle

The `ogcapi-environmental-data-retrieval-1.bundled.json` file is a standalone/portable OpenAPI document which includes all dependencies included from the components sub-directories, and is built automatically via GitHub Actions.  To test/build the bundle locally:

```bash
# install Swagger CLI via npm
npm install -g @apidevtools/swagger-cli

# generate OpenAPI bundle
cd standard/openapi
swagger-cli bundle -r -o ogcapi-environmental-data-retrieval-1.bundled.json ogcapi-environmental-data-retrieval-1.yaml
```

See also [Swagger CLI](https://apitools.dev/swagger-cli/) and its [GitHub repository](https://github.com/APIDevTools/swagger-cli).
