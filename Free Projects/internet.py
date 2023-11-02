from geopy.geocoders import Nominatim

location = "Vantaa"

location = Nominatim(user_agent="GetLoc")
getLocation = location.geocode("Vantaa")



print("Address : ", getLocation.address)
print("Latitude : ", getLocation.latitude)
print("Longitude : ", getLocation.longitude)
print("Altitude : ", getLocation.altitude)