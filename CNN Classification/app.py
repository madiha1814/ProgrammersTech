'''
Author: Najma Bibi
Email: najmabibi@gmail.com
Date: 2024-July-15
'''

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tempfile

# Load the trained model
model = load_model('tomato_model.h5')

# Function to preprocess the image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to make predictions
def predict_disease(image_path):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    labels = ['Bacterial_spot', 'Early_blight', 'Late_blight', 'Tomato___healthy', 'not_tomato_leaf']
    predicted_label = labels[np.argmax(prediction)]
    return predicted_label

# Streamlit app layout
st.title('Tomato Disease Detection')


# File uploader
uploaded_file = st.file_uploader('Upload an image of a tomato leaf to detect the disease.', type='jpg')

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', width=200)
    
    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name
    
    # Make prediction
    label = predict_disease(temp_file_path)
    st.write(f'Prediction: {label}')
