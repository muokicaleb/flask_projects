from flask import Flask
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, login_user, logout_user, current_user

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def reg():
    render_template('index.html')
