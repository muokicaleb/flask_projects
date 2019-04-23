from flask import Flask
from flask import render_template
from creds import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
import stripe


app = Flask(__name__)
stripe_keys = {
    'secret_key': STRIPE_SECRET_KEY,
    'publishable_key': STRIPE_PUBLISHABLE_KEY
}


stripe.api_key = stripe_keys['secret_key']


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


if __name__ == "__main__":
    app.run(debug=True)
