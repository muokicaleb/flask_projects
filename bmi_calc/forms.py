

from flask import Flask, request
app = Flask(__name__)

response = ""


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    if text == ' ':
        response = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number"
    elif text == '1':
        response = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"
    elif text == '1*1':
        accountNumber = "ACC1001"
        response = "END Your account number is " + accountNumber
    elif text == '1*2':
        balance = "KES 10,000"
        response = "END Your balance is " + balance
    elif text == '2':
        response = "This is your phone number " + phone_number
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
