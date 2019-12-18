# from datetime import datetime
# import os
# import pytz
import requests
# import math

with open('./api_key.txt') as f:
    API_KEY = f.read()
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def api_get_request(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as e:
        print(e)
        data = None
    return data