import streamlit as st
st.title("some basic commands like slider button etc")

age = st.slider("Enter your age",1,100)

city=st.selectbox("choose your city", ["delhi","pune","mumbai",])

if st.button("show details"):
    st.button("age",age)
    st.button("city",city)