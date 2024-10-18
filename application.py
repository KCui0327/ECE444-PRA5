from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "Hello world"

@application.route("/test", methods=["POST", "GET"])
def load_function():
    if request.method == "GET":
        return jsonify({'message': 'Send a POST request with your inputs to get predictions.'})

    inputs = request.get_json().get('inputs', None)
    if not inputs:
        return jsonify({'error': 'No inputs provided'}), 400

    ###### Model loading #####
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)

    ##########################
    # Use the model to predict
    predictions = []
    for input_text in inputs:
        prediction = loaded_model.predict(vectorizer.transform([input_text]))[0]
        predictions.append(prediction)
    

    # Return the predictions as a JSON response
    return jsonify({'predictions': predictions})

if __name__ == "__main__":
    application.run()
