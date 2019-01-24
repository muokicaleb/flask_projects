import requests
from cred import API_KEY
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    new_city = request.form.get('city')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + API_KEY

    weather_data = []

    r = requests.get(url.format(new_city)).json()

    weather = {
        'city': r['name'],
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    weather_data.append(weather)

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
