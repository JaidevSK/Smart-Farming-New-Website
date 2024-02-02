# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:09:00 2023

@author: jaide
"""


import streamlit as st
import pickle


original_title = '''<h1 style="font-family: arial; text-align: center;">Project Smart Farming</h1>
<h2 style="font-family: arial; text-align: center;">Yield Prediction based on Weather and Soil Data</h2>'''
st.markdown(original_title, unsafe_allow_html=True)
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://media.istockphoto.com/id/1147789319/photo/flowers-composition-eucalyptus-leaves-and-cotton-flowers-on-pastel-gray-background-flat-lay.webp?b=1&s=170667a&w=0&k=20&c=P-DQCiiOBA3ka32xNifm7RGVuapb0IStzyrNHBX-_SY=");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

a = st.file_uploader("Upload the csv file of the required parameters")
st.write("""
         ## OR
         """)
b = st.text_area("Write the data of the parameters in comma separated format")

s = st.button("Submit")
if s:
    model = pickle.load(open("Yield Prediction Model.sav", "rb"))
    result = model.predict(list(map(b.split(","))))
    st.write("The Predicted Yield in Kg per Hectares is:", result[0])


        

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
