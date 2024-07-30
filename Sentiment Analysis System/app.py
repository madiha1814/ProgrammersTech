'''
Author: Najma Bibi
Email: najmabibi@gmail.com
Date: 2024-July-22
'''

import streamlit as st
import pickle

# Loading the vectorizer and models
with open('vectoriser.pickle', 'rb') as file:
    vectorizer = pickle.load(file)

with open('Sentiment_LR.pickle', 'rb') as file:
    model_LR = pickle.load(file)

with open('Sentiment_BNB.pickle', 'rb') as file:
    model_BNB = pickle.load(file)

with open('Sentiment_SVC.pickle', 'rb') as file:
    model_SVC = pickle.load(file)

# Defining a function to preprocess and vectorize the text
def preprocess_text(text):
    return vectorizer.transform([text])

# Defining prediction functions for each model
def predict_with_LR(text):
    processed_text = preprocess_text(text)
    return model_LR.predict(processed_text)[0]

def predict_with_BNB(text):
    processed_text = preprocess_text(text)
    return model_BNB.predict(processed_text)[0]

def predict_with_SVC(text):
    processed_text = preprocess_text(text)
    return model_SVC.predict(processed_text)[0]

# Streamlit app
st.title("Sentiment Analysis App")

st.write("Enter your text below:")

# Text input from user
user_input = st.text_area("Input Text", "")

# Dropdown menu for model selection with Bernoulli Naive Bayes as the default selected option
model_option = st.selectbox(
    "Choose the model to predict sentiment:",
    ("Bernoulli Naive Bayes", "Logistic Regression", "Support Vector Classification")
)

# Button to predict sentiment
if st.button("Predict Sentiment"):
    if user_input:
        # Make prediction based on selected model
        if model_option == "Logistic Regression":
            prediction = predict_with_LR(user_input)
        elif model_option == "Bernoulli Naive Bayes":
            prediction = predict_with_BNB(user_input)
        else:
            prediction = predict_with_SVC(user_input)
        
        # Display the prediction result
        st.write(f"**Prediction ({model_option}):** {prediction}")
    else:
        st.write("Please enter some text to analyze.")
