import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import streamlit as st
import pandas as pd
import numpy as np
import requests
import os
import joblib

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        st.error(f"Failed to download {filename}. Status code: {response.status_code}")

# URLs for models
preprocessor_url = 'https://github.com/mahmoudmagdyhassan/Mahmoud-/blob/main/app/preprocessor%20(1).pkl'
model_url = 'https://github.com/mahmoudmagdyhassan/Mahmoud-/blob/main/app/poly%20(1).pkl'

# File paths
preprocessor_path = 'preprocessor (1).pkl'
model_path = 'poly (1).pkl'

# Download files
download_file(preprocessor_url, preprocessor_path)
download_file(model_url, model_path)

# Load models
preprocessor = joblib.load(preprocessor_path)
model = joblib.load(model_path)

# Check if both preprocessor and model are successfully loaded
if preprocessor is not None and model is not None:
    st.success("Models successfully loaded!")

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
log_price = model.predict(new_data_preprocessed) # in log scale
price = np.exp(log_price) # in original scale

# From Lakhs to USD
price_usd = price[0] * 1219

# Output
if st.button('Predict'):
    st.header('Predicted Price')
    st.write('Price in USD:', price_usd)

