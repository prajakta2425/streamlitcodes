import streamlit as st
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

st.title("some basic commands in streamlit")
name=st.text_import("Enter your name")

if st.button("submit"):
    st.write("hello",name)




