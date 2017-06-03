# distance-calc
Calculate haversine distance between current location and a list of other locations and select nearest

Requires credentials.py with api key

Requires location_list which is a list of ATM locations

May not always choose the best loctaion because it is not caluculating driving distance, only haversine distance ("as the crow flies")

Request latitude and longitude for each ATM location each time script is run -- should be modified to store those values to reduce running time

Notes for modification to make script run more quickly:
Something like this should work:

if disk cache exists:
    data = read disk cache
if thing in data and age < ttl:
    return location
location = ask google
write location to disk cache
return location

