#pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

st.title("Website of SkillEdge")

st.header("Header")

st.subheader("This is a subheader")

st.text("Welcome to our page")

st.markdown("### This is a markdown")

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)

st.write("Text with write")

st.write(range(10))

from PIL import Image #PIL - Pillow to open images
img = Image.open(r"SkillEdge_Logo.png")
st.image(img, width = 200)

if st.checkbox("Show/Hide"):
    st.text("Showing")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your Hobby is: ", hobby)

hobby = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your Hobby is: ", hobby)


st.button("Click")

if(st.button("About")):
    st.text("Welcome")

name = st.text_input("Enter your name", "Type Here...")

if (st.button('Submit')):
    result = name.title()
    st.success(result)

level = st.slider("Select the level: ", 1, 5)

st.text('selected: {}'.format(level))

data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['x', 'y']
)
st.line_chart(data)
