from flask import Flask
from flask import render_template
from flask import request
from forms import input
from bmi_calc import calc

app = Flask(__name__)
app.config['SECRET_KEY'] = '315742e65f9228cea7c3d52418hja5e3'


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    form = input(request.form)
    if request.method == 'POST' and form.validate():
        kg = float(request.form.get('weight'))
        cm = float(request.form.get('height'))
        bmi = calc(kg, cm)
    return render_template('index.html', form=form, bmi=bmi)


if __name__ == '__main__':
    app.run(debug=True)
