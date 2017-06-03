#!~/usr/bin/env/python
import googlemaps
import credentials
import gpxpy.geo
import re

currentaddr = raw_input("Input your address: ")

def location_of(location):
    gmaps = googlemaps.Client(key=credentials.api_key)
    geocode_result = gmaps.geocode(location)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    #print("Processing, please wait..\n")
    #print("Processing, please wait.\n")
    return (lat,lon)


def distance_between(loc1, loc2):
    lat1, lon1 = loc1
    lat2, lon2 = loc2
    dist = gpxpy.geo.haversine_distance(lat1,lon1,lat2,lon2)
    #print(dist)
    print("Please wait, retrieving data.\n")
    return dist

def get_atm_addresses(filespec):
    with open(filespec) as f:
        data = f.read()
    expr = re.compile(r"\s[0-9\-]+.+\w{2}\s\d{5}")
    addresses = [e[1:] for e in re.findall(expr, data)]
    return addresses

def find_closest_atms(customer, atms, limit=5):
    cloc = location_of(currentaddr)
    atm_distances = []
    for atm in atms:
        atm_location = location_of(atm)
        dist = distance_between(cloc, atm_location)
        #print("Distance to ATM at {} is {}".format(atm, dist)) 
        atm_distances.append((atm, dist))
    closest_atm_distances = sorted(atm_distances, key=lambda t: t[1])
    return closest_atm_distances[:limit]

atms = get_atm_addresses('location_list')
nearest_atms = find_closest_atms(currentaddr, atms)
print("We've located the five nearest ATMs.\n")
for atm, dist in nearest_atms:
    print("ATM at {}, {} meters away\n".format(atm,dist))


