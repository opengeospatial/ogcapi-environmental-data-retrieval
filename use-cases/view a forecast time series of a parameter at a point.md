## Obtain or view a forecast time series of a parameter at a point
**Contributed by:** @Peter Trevelyan - UK Met Office

## Typical user scenario:
The flight planner needs to be aware of the forecast of visibility for a specific location defined by a coordinate, a named place or an ICAO id over a time period. The planner is interested to know the hours for which a threshold is exceeded so they can alert of the possibility of the airport having to operate under restricted conditions. 
Generic User Goal: - Obtain or view the windows of opportunity/risk.

## Actors: 
Flight Planner, Pilot, ATC

## Preconditions:
1.	Gridded products of forecast visibility are available.
2.	A WFS web service, using a set of stored procedures that delivers to the client the time series for a parameter.

## Process: 
1.	The System determines the time period spanning the request’s context.
2.	The System determines the “best forecast” data for the specific product(s) that are valid within the time period. 
3.	For the given point, the System extracts, from the surrounding grids point, data for the specified point for each from each of the best forecasts using either “nearest neighbor” or interpolation.
4.	A Mathematical Operation will generate the time series and convert to GML.
5.	The time series expressed in GML is served by the WFS.

## Required input details:
1.	Specify point by coordinate, name or ICAO ID.
2.	Specify Time i.e. in this case the time range to be monitored with each new forecast product.
3.	Specify Product, in this case forecast visibility.
4.	The business rules to select the “best data”.

## Output format:
1.	A XML document (based on WXXM) that describes the forecast parameter for each forecast period.

## Extensions:
2.	Return the hours that the parameter crosses the threshold.
3.	The hours for which either exceeds or failed to reach the threshold.
4.	Other parameters can be added.

## Related deliverables:
1. Use case and requirements
2. Weather on the web best practice

## Related requirements
