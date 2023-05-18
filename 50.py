import streamlit as st
import pandas as pd
data =st.file_uploader("Upload a CSV")
data.head()
data.info()
