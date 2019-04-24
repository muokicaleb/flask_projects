from flask import Flask
from flask import render_template
from flask import request
from creds import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
import stripe


app = Flask(__name__)
stripe_keys = {
    'secret_key': STRIPE_SECRET_KEY,
    'publishable_key': STRIPE_PUBLISHABLE_KEY
}


stripe.api_key = stripe_keys['secret_key']


@app.route("/")
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route("/pay", methods=['post'])
def pay():
    print(request.form)


if __name__ == "__main__":
    app.run(debug=True)
