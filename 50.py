import scikit-learn





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

