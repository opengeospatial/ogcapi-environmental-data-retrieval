
## get unstructured Obs from polygon

**Contributed by:** @RichCarne - Met Office

## Typical user scenario:
Observation data is naturally unstructured in terms of its position, it should be possible for a developer to make a request for a timeseries of observation data for a given area represented by a polygon.


## Actors:
Developer Application

## Preconditions: 
1. Developer application knows area to be interrogated
2. Developer application knows time range to be returned

## Process: 
1.	The System determines the time period spanning the request’s context.
2.	The System determines the "best" data for the specific area that are valid within the time period.
3.	For the given area, the System extracts, from the best possible source all available parameters for the requested time range and area.


## Required input details:
1.	Specify area by coordinate array, in Lat Long.
2.	Specify Time range, from and too.

## Output format:
1.	A geo-Json object containing all available parameters for the time series within the specified area.

## Extensions:
1.	Developer applications may wish to filter observation parameters so as to only recieve those required
 
## Related deliverables:
1. Use case and requirements
2. Weather on the web best practice

## Related requirements:
