from flask import Flask
from flask import render_template
from forms import inputForm
from bmi import bmicalc
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = '315742e65f9228cea7c3d52418bda5e3'

bmi_value = 0


@app.route("/", methods=['GET', 'POST'])
def index():
    form = inputForm()
    if form.validate_on_submit():
        kg = form.kg.data
        height = form.cm.data
        global bmi_value
        bmi_value = bmi_value + bmicalc(kg, height)
    return render_template('index.html', form=form, bmi_value=bmi_value)


if __name__ == '__main__':
    app.run(debug=True)
