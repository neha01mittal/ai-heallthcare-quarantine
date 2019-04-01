from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd 

app = Flask(__name__)

counter = 0
clf = None
def start_runner():
    print("Hello")
    #train here
    df_final = pd.read_csv("clean_data.csv")
    y = df_final['Species']

    x = df_final.drop(['Species'], axis=1)

    #x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)
    clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=5, alpha=0.0001,
                     solver='sgd', verbose=10,  random_state=21,tol=0.000000001)
    clf.fit(x, y)
 
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
    x_test = pd.read_csv("test_data.csv")
    y_pred = clf.predict(x_test)
    print("Prediction: ", y_pred)  
    return str(resp)


@app.route("/status", methods=['GET'])
def status():

    # 2. Test format

    return str(counter)



if __name__ == "__main__":
    start_runner()
    app.run(debug=True)
