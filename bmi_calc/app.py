from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from forms import input
from bmi_calc import calc

app = Flask(__name__)

bmi = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    form = input(request.form)
    if request.method == 'POST' and form.validate():
        kg = form.weight.data
        cm = form.height.data
        bmi = calc(kg, cm)
    render_template('index.html', form=form, bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
