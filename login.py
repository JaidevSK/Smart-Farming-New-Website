# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:36:27 2023

@author: jaide
"""

import streamlit as st

original_title = '''<h1 style="font-family: arial; text-align: center;">Project Smart Farming</h1>
<h2 style="font-family: arial; text-align: center;">Login Page</h2>'''
st.markdown(original_title, unsafe_allow_html=True)

warn = '''<p style="font-family: arial; text-align: center;background-color:Tomato;">Authentication Failed. Reload and Try Again... ⚠️</p>'''
success = '''<p style="font-family: arial; text-align: center;background-color:Green;">Authentication Successful</p>'''

u=st.text_input("", value="Enter your Username")
p=st.text_input("", value="Enter your Password")
if st.button("Submit"):
    if u=="username" and p=="password":
        st.markdown(success, unsafe_allow_html=True)
        st.link_button("Go to Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/")
    else:
        st.markdown(warn, unsafe_allow_html=True)
        

# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://github.com/JaidevSK/Smart-Farming-New-Website/blob/main/Background%20Image.jpg?raw=true");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)