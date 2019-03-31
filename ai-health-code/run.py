from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

counter = 0
def start_runner():
    print("Hello")
    #train here

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    #1.
    resp = MessagingResponse()

    # Determine the right reply for this message
    resp.message("We are looking into fixing your " + body)

    global counter
    counter += 1

    #2. Test format

    return str(resp)


@app.route("/status", methods=['GET'])
def status():

    # 2. Test format

    return str(counter)



if __name__ == "__main__":
    start_runner()
    app.run(debug=True)
