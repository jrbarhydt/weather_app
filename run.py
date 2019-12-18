from pprint import pprint as pp
from flask import Flask, render_template, request
from WeatherApp import api_get_request
import pandas as pd

df = pd.read_csv('cities.csv')
data = [{'name': city[0]} for city in df.values]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html', data=data)


@app.route("/result", methods=['GET', 'POST'])
def result():
    weather_data = []
    error = None
    comp_select = request.form.get('comp_select')
    resp = api_get_request(comp_select)
    pp(resp)
    if resp:
        weather_data.append(resp)
        if len(weather_data) != 2:
            error = 'Bad Response from Weather API'
    return render_template('weather.html', data=weather_data, error=error)


if __name__ == '__main__':
    app.run(debug=True)
