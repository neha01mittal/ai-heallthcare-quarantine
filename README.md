## About the Project
Project name: Quar-in-time
Team: Bamidele Elegbede (designer), Neha Mittal (engineer), Inez Wihardjo (business)
Event: Accenture School of AI #HealthHack, San Francisco

## Background
H5N1 Bird Flu Influenza killed 14,000 people in 2009. But because we did not act fast enough, the same set of chickens bearing the diseases are exported. The disease that are borne by chickens in China killed even more people in Hong Kong and other parts of the world.

The worst part is, in less developing countries, underreporting is a big problem.
Does it make sense that in Australia, there are 21.6% of the population facing food borne diseases but in a country like Nigeria there are only 0.05%? The main reason is because of lack of access to healthcare and awareness, there are major underreporting.

### Quar-in-time
Quar-in-time is an AI tool that enables local community and governments act faster to respond to viral outbreaks in developing countries. 

We offer a holistic platform to gather crowdsourced information on trends of symptoms, alert government bodies of abnormalities, and diagnose the root cause to truly kill the outbreak.

Every second counts. Individuals can be encouraged to share about their health issues and help health officials understand better about outbreaks happening in the region.


## Quar-in-time Overview
### Inform.
Due to lack of internet access in developing countries, we created a SMS-based chatbot that prompts Individuals from the community to share info about their symptoms, and dig information about the food they eat.

### Discover.
Using our AI algorithm, our machine then predicts whether these individuals are actually victims of a particular foodborne disease outbreak. This is done by training our model with datasets of foodborne diseases that happen in other parts of the world.

### Alert.
Once the outbreak reaches a critical level, our system issues alerts to relevant organization bodies, such as governments (to issue travel bans, activate quarantines), healthcare organization (to reallocate resources), and retailers (to cut their supply chain).

## Demo Procedure
### Getting started
To start the dashboard:

     run npm install from template folder

     hit localhost:5000


To start the python service:

     python run.py (This script contains the code to train the model and make predictions on the test data)

Send an SMS to +1 203 806 9336 (our hotline), with the text “000” to activate the chatbot. Note: Since we used a Twilio trial account, you need to register your phone number to activate the demo.

Answer the chatbot prompts based on symptoms and food that you actually ate in the last 24 hours.

Open the dashboard.

Due to limited time, we scoped out the dashboard to show the following effects:

     Show how the # of reports has increased

     Log your entry with the various inputs (i.e. symptoms, food eaten, place of consumption, time stamp, GPS stamp)

     Plot out the trend overtime of the food-borne diseases in the region

     Indicate the location of the outbreak on a map
		

## Quar-in-time Tech Stack
We used a Twilio to interface the SMSes sent between our system and the individual patients.

We used Twilio’s Rest API to receive the users’ data points
We parsed the given set of information to format it in a manner that is consumable by our AI algorithm.
We have a Get API on Python flask that sends this prediction results to our monitoring dashboard.
The prediction model takes in training data from an open-source data found from Kaggle <link here>. We used one hot vectorization to flatten out the following categorical features. That are:
Location of the individual (i.e. GPS coordinates)
Food items (e.g. beef, chicken, seafood, etc)
Symptoms (e.g. diarrhoea, fever, etc)
Place of consumption (e.g. restaurants or at-home)
The prediction model is a multinomial classification problem that predicts the type of foodborne diseases based on the given inputs.
Various Algorithm Results
We tried various AI models and achieved the following level of prediction accuracies:

## Models
### Multinomial Logistic Regression
35%
### Random Forest Classifier
58%
### Decision Tree Classifier
30%
### Neural Nets
65%

## Next Steps
### Time series
We would like to use the time of the SMS submissions to timestamp the datasets and truly understand the trend patterns over time. Particularly, we would use the timestamps to create epoch windows and perform time series analysis. This way, we could truly leverage on the power of crowdsourcing more effectively.

### Hypertuning
Ideally we would look into hypertuning the various parameters through a validation dataset.

### Cross-validation
If we had a larger data pool, we would split up some of the known datasets and use it to cross-validate our algorithm.



