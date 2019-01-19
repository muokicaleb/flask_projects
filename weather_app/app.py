import requests
from cred import API_KEY
from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


global new_city


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        new_city = request.form.get('city')
    if new_city:
        new_city_obj = City(name=new_city)
        db.session.add(new_city_obj)
        db.session.commit()

    cities = City.query.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + API_KEY
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'], }
        weather_data.append(weather)

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
