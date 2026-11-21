import streamlit as st
st.title("Hello William")
st.write("My firt app is live!")

name = st.text_input("What is your name?")
if name:
  st.success(f"Welcome,{name}!")
