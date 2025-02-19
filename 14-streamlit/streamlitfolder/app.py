import streamlit as st
import pandas as pd
import numpy as np

# Title of application
st.title("Hello Streamlit")

st.write("This is a simple text")

# create a simple dataframe 

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[4,5,8,10]
})

# creation of a dataframe
st.write("Here is the dataframe")
st.write(df)

# create a line chart 

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
