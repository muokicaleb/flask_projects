from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
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


@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html')


@app.route("/pay", methods=['post'])
def pay():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=500,
        currency='usd',
        description='Product'
    )
    return redirect(url_for('thankyou'))


if __name__ == "__main__":
    app.run(debug=True)
