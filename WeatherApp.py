# from datetime import datetime
# import os
# import pytz
import requests
# import math

API_KEY = '20c425a816917e3f827ce93d19c0a6d1'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def api_get_request(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data