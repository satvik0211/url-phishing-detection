from extractor import extract_features
import streamlit as st
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))

st.title("URL Predictor")

input_url=st.text_area("Enter Your URL")

transform = extract_features(input_url)

urlss= np.array(transform).reshape(1,-1)

if st.button("predict"):

    result = model.predict(urlss)

    if result == 1:
        st.header("Malicious")
    else:
        st.header("safe")

