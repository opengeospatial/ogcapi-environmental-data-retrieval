
## Scientific toolset integration

**Contributed by:** @m-burgoyne - UK Met Office

## Typical user scenario:
Use a Jupyter notebook to create and share documents that contain live code, equations, visualisations and narrative text. 

## Actors:
Developer Application

## Preconditions:
1. Developer application knows data to be interrogated
2. Developer application knows which query types are supported
3. Developer application knows location to be interrogated
4. Developer application knows time range to be returned
5. Developer application knows output format to be returned

## Process:
1. The System determines the geospatial location of the request's context.
2. The System determines the time period spanning the request’s context.
3. The System determines the data type (e.g. rain, snow) relevant to the request's context.
4. The System transforms the data into the output format relevant to the requests context
5. For the given location, time period and weather radar data type, the System provides the data requested

## Required input details:
1. Specify query type
2. Specify location (coordinates)
3. Specify time period
4. Specify data parameters
5. Specify output format


## Extensions:
 
## Related deliverables:
1. Use case and requirements
2. Environmental Data API best practice

## Related requirements:
