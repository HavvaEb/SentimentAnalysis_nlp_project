# main.py
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    data = pd.read_csv("Rev_cleaned.csv")
    text = request.form['text']
    
    
    my_txt = pd.Series(text)
    
    data = data.dropna()
    X = data["Text"]
    new_comment = CountVectorizer().fit(X).transform(my_txt)
    
    
    log_model = pickle.load(open('model_NLP.pkl', 'rb'))
    
    label = log_model.predict(new_comment)
    if label == 1:
        decision = 'This sentence is positive!'
    else:
        decision = 'This sentence is negative!'
    
    return(render_template('index.html', variable=decision))

if __name__ == "__main__":
    app.run(port='8088', threaded=False, debug=True)

