# ai-heallthcare-quarantine

### Dashboard: 

To start the dashboard: 

1. run npm install from template folder
2. hit localhost:5000

### To start the python service:
python run.py 

This script contains the code to train the model and make predictions on the test data


### The flow:

As soon as a text message is sent (using Twilio), the dashboard is notified and the neural net starts predicting possible reasons for the symptoms indicated in the text message. Finally the dashboard is notified of the final ML prediction
