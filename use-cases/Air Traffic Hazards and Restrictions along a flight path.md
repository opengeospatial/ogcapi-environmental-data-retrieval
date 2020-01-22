# Obtain or view Air Traffic Hazards and Restrictions along a flight path

**Contributed by:** @Peter Trevelyan - UK Met Office

## Typical user scenario:
A flight is planned to take off from Heathrow and land in Denver. The pilot is given the flight details in terms of time to cruise, cruising altitude, way points and time for descent. The pilot and flight planner need to be made aware of any forecast significant weather conditions that might be encountered.  All warning text messages such as VAA, SIG/AIRMET that intersect the flight path need to be identified and passed to the pilot and flight planner.
Generic User Goal: - Obtain or view warning products within a flight path in the past, present, or future.

## Actors: Flight Planner, Pilot, ATC
## Preconditions:
1.	Volcanic Ash data available as WXXM.
2.	SIGMETS, NOTAMS and AIRMETS available and stored such that they can be indexed using geospatial attributes.

## Process: 
1.	An analysis of all the messages to search for which AIR/SIGMETS, VAA that intersect the lateral corridor, note that the vertical dimension, if given, is ignored.
2.	As above, but using the vertical extent, if given.
3.	The System determines the time period spanning the request’s context, as specified. 
4.	The System determines the specific observational products that are contained within the corridor. 
5.	The System returns the relevant text messages

## Required input details:
1.	Specify the exchange protocol, in this case, WFS.
2.	Specify a Corridor; a trajectory is specified by the user as a set of way points with a vertical and horizontal extent (if specified).
3.	Specify Time i.e. the start time and end time of the flight. This might be extended by the adding time to cruise and time for descent.
4.	Specify Product i.e. SIGMET, AIRMET, VAA, NOTAMS; 
## Output format:

1.	A XML document (based on WXXM) that contains all the relevant messages.

## Extensions:
1.	One too many products may be requested. 
2.	If no times are included, then the current time is assumed.
3.	Tropical cyclones advisories may be added.
 
## Related deliverables:
1. Use case and requirements
2. Weather on the web best practice

## Related requirements
