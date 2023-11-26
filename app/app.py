
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import joblib

model_url = "https://github.com/mahmoudmagdyhassan/Mahmoud-/raw/main/app/poly%20(1).pkl"
preprocessor_url = "https://github.com/mahmoudmagdyhassan/Mahmoud-/raw/main/app/preprocessor%20(1).pkl"

# Download and load models
model_content = requests.get(model_url).content
preprocessor_content = requests.get(preprocessor_url).content

model = pickle.loads(model_content)
preprocessor = pickle.loads(preprocessor_content)

# Rest of your Streamlit app code...

# Input Data
location = st.selectbox('Location', ['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad'])
year = st.number_input('Year')
km_driven = st.number_input('Kilometers Driven')
fuel_type = st.selectbox('Fuel Type', ['Diesel', 'Petrol', 'CNG', 'LPG'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner_type = st.selectbox('Owner Type', ['First', 'Second', 'Third', 'Fourth & Above'])
mileage = st.number_input('Mileage')
engine = st.number_input('Engine')
power = st.number_input('Power')
seats = st.number_input('Seats')
car_model = st.text_input('Model')

# Preprocessing
new_data = {'Location': location, 'Year': year, 'Kilometers_Driven': km_driven, 'Fuel_Type': fuel_type, 'Transmission': transmission,
         'Owner_Type': owner_type, 'Mileage': mileage, 'Engine': engine, 'Power': power, 'Seats': seats, 'Model': car_model}
new_data = pd.DataFrame(new_data, index=[0])
new_data.Owner_Type = new_data.Owner_Type.map({'First':1, 'Second':2, 'Third':3, 'Fourth & Above':4})
new_data_preprocessed = preprocessor.transform(new_data)

# Prediction
log_price = model.predict(new_data_preprocessed)  # in log scale
price = np.exp(log_price)  # in original scale

# From Lakhs to USD
price_usd = price[0] * 1219

# Output
if st.button('Predict'):
    st.header('Predicted Price')
    st.write('Price in USD:', price_usd)
