api_key = '29be9566cf3d7be7b236f359a2d10d5c'

from geopy.geocoders import Nominatim
import requests

location = Nominatim(user_agent="GetLoc")

city = input("Insert city:> ")
getLocation = location.geocode(city)

print("Receiving city coordinates ...")
lat = getLocation.latitude
lon = getLocation.longitude
print(lat, lon)

print("Calling weather service ...")

call_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
req = requests.get(call_weather).json()

temp = req['main']['temp']

print(f" It is {temp - 273.15:.1f} C outside in {city}.")