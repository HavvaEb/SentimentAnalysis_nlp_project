# sentiment_analysis_nlp
Scheduale

- Project: 'Sentiment Analysis'
- Duration : '9 days'
- Presentation: '01/07/2022 10:00 AM'
- Challenge: 'Solo'
## Description
I just got an internship at Amazon. As a first task, they ask me to analyze people's reaction to their products to improve their marketing practices. This dataset consists of a few million Amazon customer reviews (input text) and star ratings (output labels) for learning how to train a model for sentiment analysis.

## Host organization:
<a href="https://github.com/becodeorg"><strong>BeCode</strong></a>(Ghent campus)
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200">

## Client organization:

![Amazon](https://upload.wikimedia.org/wikipedia/commons/6/62/Amazon.com-Logo.svg)

## Mission objectives

- Be able create a sentiment analysis model using NLP.
- Be able to deploy your model.
## Usage

- Preprocess the data.
- Create a sentiment analysis model.
- Evaluate model just to Make sure its predicting right.
- Predict the overall sentiment.
- Randomly check a few tweets to verify that my model predicts the right sentiment.
- Make an API that accepts a hashtag in the route `/predict`.
- Run the complete pipeline to predict the sentiment.
- Deploy it on Heroku.
## App Usage:
To open the heroku application, follow the link [Heroku](https://sentiment-analysis-havva.herokuapp.com/)
## Contributor

- #### [Havva Ebrahimi Pour](https://github.com/HavvaEb)
    - https://www.linkedin.com/in/havva-ebrahimi-pour/


## A final word of encouragement

“The lottery is a tax on people who don't understand the statistics.”
_- Anonymous_

![Cheap sentiment!](https://media.giphy.com/media/QUTt5Dt63UOQM/giphy.gif)

## Repo Architecture 

```

│   README.md                     : This file
│   data                          : contains raw data 
___
|   Other data                    : contains preprocessed and cleaned data
___                 

│   |requirements.txt             : conatins libraries require for running the heroku NLP app.
│___ 

│    app.py                       : contains script for running the heroku NLP app.
___ 
|    Notebooks
    |Nltk_Finalnotebook.ipynb
    |preprocessing_modeling_notebook.ipynb
    |CNN_RNN_notebook.ipynb  
___
|   templates                      : contains html scripts    

