from flask import Flask
from forms import RegistrationForm, LoginForm
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, login_user, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = '315742e65f9228cea7c3d52418bda5e3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager = init_app(app)
login_manager.login_view = '/'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(50))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=['GET', 'POST'])
def reg_log_form():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit() and reg_form.submit_signup.data:
        hashed_password = generate_password_hash(reg_form.password.data, method='sha256')

        new_user = User(username=reg_form.username.data,
                        email=reg_form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return "Success"
    log_form = LoginForm()

    if log_form.validate_on_submit():
        user = User.query.filter_by(username=log_form.username.data).first()
        if user:
            if check_password_hash(user.password, log_form.password.data):
                return "<h1>login Successfull</h1>"

    return render_template('index.html', reg_form=reg_form, log_form=log_form)


if __name__ == "__main__":
    app.run(debug=True)
