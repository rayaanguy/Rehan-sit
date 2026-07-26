import streamlit as st

st.sidebar.header("title")
title = st.sidebar.text_area("Description","title")
st.sidebar.header("text")
text = st.sidebar.text_area("Text","this is the text")

st.title(title)
st.write(text)

