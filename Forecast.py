import requests
import os
from datetime import datetime

# Environment key
key = os.environ.get('WEATHER_KEY')

# Exception
try:
    # Ask user to input city and name
    city = input('Enter city name: ')
    country = input('Enter country code: ')
    query = {'q': city + ',' + country, 'units': 'imperial', 'appid': key}

    # API url
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    # getting data from request
    data = requests.get(url, params=query).json()

    # print forecast with local time which is important for the user
    forecast_items = data['list']
    weather = forecast_items[0]

    timestamp = weather['dt']
    date = datetime.fromtimestamp(timestamp)
    temp = weather['main']['temp']
    desc = weather['weather'][0]['description']
    humidity = weather['main']['humidity']
    wind = data['list'][0]['wind']['speed']
    print(f'at {date}: Weather is: {desc}, Temperature is: {temp}°F, wind Speed at: {wind}, Humidity at: {humidity}')
except TypeError as e:
    print(e)
except KeyError:
    print(data['message'])
