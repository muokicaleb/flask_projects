from flask import Flask
from forms import RegistrationForm, LoginForm
from flask import render_template
from flask import url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '315742e65f9228cea7c3d52418bda5e3'


@app.route("/", methods=['GET', 'POST'])
def reg_log_form():
    reg_form = RegistrationForm()
    log_form = LoginForm()
    return render_template('index.html', reg_form=reg_form, log_form=log_form)


if __name__ == "__main__":
    app.run(debug=True)
