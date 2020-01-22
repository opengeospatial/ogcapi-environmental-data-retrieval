## Get Parameters for point across a timeseries
**Contributed by:** @RichCarne - UK Met Office

## Typical user scenario:
Developers creating applications requireing simple access to weather infromation at surface level wish to make a position based requests which result in a collection of weather parameters being returned for a specified time period. It should be possible for the request to be made both forwards and backwards from the current time.

## Actors: 
Developer Application

## Preconditions:
1. Developer application knows position to be interrogated
2. Developer application knows time range to be returned

## Process: 
1.	The System determines the time period spanning the request’s context.
2.	The System determines the "best" data for the specific location that are valid within the time period.
3.	For the given point, the System extracts, from the best possible source all available parameters for the requested time range.


## Required input details:
1.	Specify point by coordinate, in Lat Long.
2.	Specify Time range, from and too.

## Output format:
1.	A geo-Json object containing all available parameters for the time series at the specified point

## Extensions:
1. Where multiple providers of data for a given point are available, it may be possible to allow the developer application to select between sources.
2. It may be possible to allow the developer application to request data for a specific point from multiple (two or more) data suppliers
3. Developer applications may request data from multiple points simultaneously, returing parameters for time series at each point requested

## Related deliverables:
1. Use case and requirements
2. Weather on the web best practice

## Related requirements
