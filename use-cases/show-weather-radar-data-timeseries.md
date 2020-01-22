
## Show Weather Radar Data timeseries

**Contributed by:** @tomkralidis - Meteorological Service of Canada

## Typical user scenario:
Displaying radar imagery from a given time range.  The scope is a national context
radar visualization application displaying near real-time radar atop other
GIS layers (basemap/topography, placenames).

## Actors:
Developer Application

## Preconditions:
1. Developer application knows position to be interrogated
2. Developer application knows time range to be returned
3. Developer application knows the weather radar data type to be returned

## Process:
1. The System determines the geospatial location of the request's context.
2. The System determines the time period spanning the request’s context.
3. The System determines the weather radar data type (e.g. rain, snow) relevant to the request's context.
4. For the given location, time period and weather radar data type, the System provides a list of weather radar data images

## Required input details:
1. Specify location (lat, long, bounding box)
2. Specify time period
3. Specify weather radar data type

## Output format:
1. a JSON object containing links to all relevant weather radar data images
2. an animated image based on all relevant weather radar data images
3. a multipart response of all relevant weather radar data images

## Extensions:
 
## Related deliverables:
1. Use case and requirements
2. Weather on the web best practice

## Related requirements:
