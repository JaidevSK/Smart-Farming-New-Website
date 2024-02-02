# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:01:07 2023

@author: jaide
"""

import PIL
import streamlit as st


st.set_page_config(
    page_title="Field Image Viewer",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded"
)



original_title = '''<h1 style="font-family: arial; text-align: center;">Project Smart Farming</h1>
<h2 style="font-family: arial; text-align: center;">Field Image Viewer</h2>'''
st.markdown(original_title, unsafe_allow_html=True)
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://github.com//JaidevSK//Smart-Farming-New-Website//blob//main//soil_image.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

f_5m=PIL.Image.open("img5m.jpg")
f_30m=PIL.Image.open("img30m.jpg")
f_50m=PIL.Image.open("img50m.jpg")
f_100m=PIL.Image.open("img100m.jpg")
f_120m=PIL.Image.open("img120m.jpg")
st.markdown("<h1 style='text-align: center;'>Field Map (Drone View)</h1>", unsafe_allow_html=True)


height = st.select_slider('Altitude', options=[10,30,50,75,100])
v_range = st.slider('Select the %range of the vertical part of the image to be seen', 0.0, 100.0, (25.0, 75.0))
h_range = st.slider('Select the %range of the horizontal part of the image to be seen', 0.0, 100.0, (25.0, 75.0))
date = st.date_input("Select the date of the data to be seen")

if height==10:
    width, height = f_5m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_5m1 = f_5m.crop((left, top, right, bottom))
    st.image(f_5m1)
    
elif height==30:
    width, height = f_30m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_20m1 = f_30m.crop((left, top, right, bottom))
    st.image(f_20m1)
elif height==50:
    width, height = f_50m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_50m1 = f_50m.crop((left, top, right, bottom))
    st.image(f_50m1)
elif height==75:
    width, height = f_100m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_80m1 = f_100m.crop((left, top, right, bottom))
    st.image(f_80m1)
elif height == 100:
    width, height = f_120m.size
    left = (width/100)*h_range[0]
    top = (height/100)*v_range[0]
    right = (width/100)*h_range[1]
    bottom = (height/100)*v_range[1]
    f_100m1 = f_120m.crop((left, top, right, bottom))
    st.image(f_100m1)


        

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
