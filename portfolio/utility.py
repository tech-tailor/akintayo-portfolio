#!/usr/bin/activate
"""utility fuction to do diverse things"""

import requests
import math


def get_address_from_coordinates(lat, lng, api_key):
    """Get the address of a location with the longitude and latitude"""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data and data['results']:
        return data['results'][0]['formatted_address']
    else:
        return "Address not found"



def distance_calculator(lat1, lon1, lat2, lon2):
    """we use the Haversine formula
        a = sin²(Δφ/2) + cos(φ1) * cos(φ2) * sin²(Δλ/2)
        c = 2 * atan2( √a, √(1-a) )
        d = R * 
        φ1, φ2 are the latitudes of the two points in radians
        Δφ is the difference between latitudes
        Δλ is the difference between longitudes
        R is the Earth's radius (mean radius = 6,371 km)
        d is the distance between the two points
    """

    R = 6371.0  # Earth radius in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

# Example usage
lat1 = 8.934533
lon1 = 7.332849
lat2 = 8.93589
lon2 = 7.32919

distance = distance_calculator(lat1, lon1, lat2, lon2)
print("Distance:", distance, "km")
