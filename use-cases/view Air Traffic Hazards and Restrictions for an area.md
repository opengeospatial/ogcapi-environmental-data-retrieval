## Obtain or view Air Traffic Hazards and Restrictions for an area
**Contributed by:** @Peter Trevelyan - UK Met Office

## Typical user scenario:
A flight is planned to take off from Heathrow to land in Denver and the flight planner needs to know which FIRs (Flight information regions) to avoid, if possible. All possible warning text messages such as VAA, SIG/AIRMET that overlap a FIR need to be identified and passed to the flight planners.
Generic User Goal: - Obtain or view weather conditions within an area in the past, present, or future.

## Actors: 
Flight Planner, Pilot, ATC

## Preconditions:
1.	Volcanic Ash data available in HoraceV either as gridded field or WXXM.
2.	SIGMETS, NOTAMS and AIRMETS available and stored such that they can be indexed using geospatial attributes.

## Process: 
1.	An analysis of all the stored messages to search for AIR/SIGMETS, VAA that intersect the polygon;
2.	The System determines the time period spanning the request’s context, as specified.
3.	The System determines the specific warning text products i.e. AIR/SIGMETS and VAA that intersect the specified area and time period.
4.	The System returns the text messages using a WFS

## Required input details:
1.	Specify the exchange protocol, in this case, WFS.
2.	Specify a named polygon, either one created on the fly or a pre-existing named region e.g. a FIR;
3.	Specify a time period;
4.	Specify Product i.e. SIGMET, AIRMET, VAA 

## Output format:
1.	A XML document (based on WXXM) that contains all the relevant messages.

## Extensions:
1.	One too many products may be requested. 
2.	If no times are included, then the current time is assumed.
3.	Tropical cyclone advisories to be included.

## Related deliverables:
1. Use case and requirements
2. Weather on the web best practice

## Related requirements
