numpy==1.20.1

streamlit==0.76.0

seaborn==0.11.1

matplotlib==3.4.1

plotly==4.14.3

pandas==1.2.3

joblib==0.16.0

scikit-learn



import streamlit as st
import pandas as pd
data =st.file_uploader("Upload a CSV")
from sklearn.linear_model import LinearRegression

def train_model(data):

	

	X = data.iloc[0,:1]

	y = data[0,1:]

	

	model = LinearRegression()

	model.fit(X, y)

	return model

