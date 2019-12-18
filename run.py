from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from WeatherApp import api_get_request
import pandas as pd

df = pd.read_csv('cities.csv')
data = [{'name': city[0]} for city in df.values]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('weather.html', data=data)


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = api_get_request(select)
    pp(resp)
    if resp:
        data.append(resp)
        if len(data) != 2:
            error = 'Bad Response from Weather API'
    return render_template('result.html', data=data, error=error)


if __name__ == '__main__':
    app.run(debug=True)
