import requests
import time
import os
from datetime import datetime

# Environment key
key = os.environ.get('WEATHER_KEY')


# Ask user to input city and name
city = 'minneapolis'
country = 'us'
query = {'q': city + ',' + country, 'units': 'imperial', 'appid': key}

# API url
url = 'https://api.openweathermap.org/data/2.5/forecast'
# getting data from request
data = requests.get(url, params=query).json()

# print forecast with local time which is important for the user
forecast_items = data['list']
weather = forecast_items[0]

timestamp = weather['dt']
# Using UTC time because local time varies according where users are located
# daylight saving time , some days could have 23 hours and some could have 25 hours
date = datetime.fromtimestamp(timestamp)
temp = weather['main']['temp']
desc = weather['weather'][0]['description']
humidity = weather['main']['humidity']
wind = data['list'][0]['wind']['speed']
# Unix time
print(time.time())
# Output
print(f'at {date}: Weather is: {desc}, Temperature is: {temp}°F, wind speed at: {wind}, Humidity at: {humidity}')

