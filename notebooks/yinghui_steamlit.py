#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd

def load_image_model():
    model = "some model"
    return model

model = load_image_model()

st.markdown("""# Movie Genre Predictor
## Something""")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload image", type=['png', 'jpg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image)

    else:
        st.text("Please upload an image file (file type: jpg, png)")

    st.header("Your Poster")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("The Movie Genre is...")
   st.markdown('XXX and YYY')


# st.markdown("""# This is a header
# ## This is a sub header
# This is text""")

# df = pd.DataFrame({
#     'first column': list(range(1, 11)),
#     'second column': np.arange(10, 101, 10)
# })

# # this slider allows the user to select a number of lines
# # to display in the dataframe
# # the selected value is returned by st.slider
# line_count = st.slider('Select a line count', 1, 10, 3)

# # and used to select the displayed lines
# head_df = df.head(line_count)

# head_df
