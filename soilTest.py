# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:56:26 2023

@author: jaide
"""


import streamlit as st
import pickle


original_title = '''<h1 style="font-family: arial; text-align: center;">Project Smart Farming</h1>
<h2 style="font-family: arial; text-align: center;">Soil Suitability Analysis</h2>'''
st.markdown(original_title, unsafe_allow_html=True)
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://t3.ftcdn.net/jpg/01/70/76/38/360_F_170763832_QsK69yVd3sxxbVEJE5zgiw03u4kdJAca.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

# container = st.container(border=True)

# container_image = """
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-color: white;
#     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
#     background-position: center;  
#     background-repeat: no-repeat;
# }
# </style>
# """


st.markdown('<style>background-color: Blue;</style>',unsafe_allow_html=True)

typ = st.radio("How would you like to use this?", ["Soil Suitability Map Generator", "Individual Sample Testing"])

if typ == "Soil Suitability Map Generator":
    st.file_uploader("Input the .csv file of the Field")
else:
    n=st.number_input("Enter the Value of N")
    p=st.number_input("Enter the Value of P")
    k=st.number_input("Enter the Value of K")
    ph=st.number_input("Enter the Value of pH")
    s=st.number_input("Enter the Value of Salinity")
    mc=st.number_input("Enter the Value of Moisture Content")
    tem=st.number_input("Enter the Value of Temperature")
    s = st.button("Submit")
    if s:
        model = pickle.load(open("Soil Suitability Test Model.sav", "rb"))
        result = model.predict([[n, p, k, ph, s, mc, tem]])
        st.write("The Soil is Suitability Index is:", result[0])
    

st.sidebar.link_button("Go to 📷 Image Viewer", "https://project-smart-farming-zdgdgxvdjwjhzdjayfsoyj.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌵 Weed Density Visualiser", "https://project-smart-farming-ztxhdu7jtbbvnpgpujlfdg.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 💮 Yield Prediction Page", "https://project-smart-farming-bbtrh6txamftuhp2svgrf4.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🟫 Soil Suitability Analysis Page", "https://project-smart-farming-rl8ttyplxcidujmvjqzdtt.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🍀☘️ Type-Wise Weed Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌱 Crop Density Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌺 Cotton Bud Lifecycle Stage Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🍂🐞Disease, Pest and Deficiency distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🥦 Cotton Bud Counter and Visualiser Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌩️ Weather Page", "https://mausam.imd.gov.in/imd_latest/contents/satellite.php", use_container_width=True)
st.sidebar.link_button("Go to 🤖 Chat Bot App", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app", use_container_width=True)
st.sidebar.link_button("Go to 🖥️ Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/", use_container_width=True)


