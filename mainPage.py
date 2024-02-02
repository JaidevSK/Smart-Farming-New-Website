# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:56:54 2023

@author: jaide
"""

import streamlit as st



original_title = '''<h1 style="font-family: arial; text-align: center;">Project Smart Farming</h1>
<h2 style="font-family: arial; text-align: center;">Main Page</h2>
<p style="font-family: arial; text-align: center;   background-color: white;border-style: rounded;">This page containes links to all the other pages</p>'''
st.markdown(original_title, unsafe_allow_html=True)
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

st.link_button("Go to 📷 Image Viewer", "https://project-smart-farming-zdgdgxvdjwjhzdjayfsoyj.streamlit.app/",  use_container_width=True)
st.link_button("Go to 🌵 Weed Density Visualiser", "https://project-smart-farming-ztxhdu7jtbbvnpgpujlfdg.streamlit.app/", use_container_width=True)
st.link_button("Go to 💮 Yield Prediction Page", "https://project-smart-farming-bbtrh6txamftuhp2svgrf4.streamlit.app/", use_container_width=True)
st.link_button("Go to 🟫 Soil Suitability Analysis Page", "https://project-smart-farming-rl8ttyplxcidujmvjqzdtt.streamlit.app/", use_container_width=True)
st.link_button("Go to 🍀☘️ Type-Wise Weed Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.link_button("Go to 🌺 Cotton Bud Lifecycle Stage Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.link_button("Go to🍂🐞 Disease, Pest and Deficiency distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.link_button("Go to 🥦 Cotton Bud Counter and Visualiser Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.link_button("Go to 🌩️ Weather Information Page", "https://mausam.imd.gov.in/imd_latest/contents/satellite.php", use_container_width=True)
st.link_button("Go to 🤖 Chat Bot App", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/", use_container_width=True)
st.link_button("Go to 🖥️ Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/", use_container_width=True)



st.sidebar.link_button("Go to 📷 Image Viewer", "https://project-smart-farming-zdgdgxvdjwjhzdjayfsoyj.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌵 Weed Density Visualiser", "https://project-smart-farming-ztxhdu7jtbbvnpgpujlfdg.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 💮 Yield Prediction Page", "https://project-smart-farming-bbtrh6txamftuhp2svgrf4.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🟫 Soil Suitability Analysis Page", "https://project-smart-farming-rl8ttyplxcidujmvjqzdtt.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🍀☘️ Type-Wise Weed Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌺 Cotton Bud Lifecycle Stage Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🍂🐞Disease, Pest and Deficiency distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🥦 Cotton Bud Counter and Visualiser Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌩️ Weather Page", "https://mausam.imd.gov.in/imd_latest/contents/satellite.php", use_container_width=True)
st.sidebar.link_button("Go to 🤖 Chat Bot App", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app", use_container_width=True)
st.sidebar.link_button("Go to 🖥️ Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/", use_container_width=True)


# Login Page
# Main Page
# Data Uploading Page
# Datalog
# Image Viewer
# Weed Density Analyser
# diseases, pests, deficiencies
# cotton buds ctr
# weed type
# cotton lifecycle
# crop coverage
# soil suitability
# yield prediction
# weather, prices, other info


