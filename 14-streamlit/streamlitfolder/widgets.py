import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit Text Input")

# takes the name input
name = st.text_input("Enter your name")

# creation of a slider
age = st.slider("Select your age:",0,100,10)

st.write(f"Your age is {age}")

options = ["Python","Java","C++","Javascript"]
choice = st.selectbox("Choose your favorite language:",options)
st.write(f"You selected {choice}")

# if the name exists then print hello followed by the name
if name:
    st.write(f"Hello, {name}")

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[4,5,8,10]
})

data = {
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    "City":["New york","Los angeles","Chicago","Houston"]
}

df = pd.DataFrame(data)
df.to_csv("file.csv")
st.write(df)

# creation of a dataframe
st.write("Here is the dataframe")
st.write(df)


uploaded_file = st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)