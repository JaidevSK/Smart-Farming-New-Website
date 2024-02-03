# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import cottonLifeCyclesettings as settings
import cottonLifeCyclehelper as helper

# Setting page layout
st.set_page_config(
    page_title="Cotton Life Cycle Stage Detector",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i0.wp.com/www.figandbloom.com/wp-content/uploads/2017/10/Depositphotos_10212026_l-2015.jpg?fit=1024%2C680&ssl=1");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# Main page heading
st.markdown("<h1 style='text-align: center;'>Cotton Life Cycle Stage Detector</h1>", unsafe_allow_html=True)
# Sidebar
st.sidebar.header("Select the Configuration")

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 40)) / 100

# # Selecting Detection Or Segmentation
# if model_type == 'Detection':
#     model_path = Path(settings.DETECTION_MODEL)
# elif model_type == 'Segmentation':
#     model_path = Path(settings.SEGMENTATION_MODEL)
model_path = Path(settings.DETECTION_MODEL)


# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)


source_img = None
# If image is selected
source_img = st.sidebar.file_uploader(
    "Choose an image...", type=("jpg", "jpeg", "png"))

col1, col2 = st.columns(2)

with col1:
    try:
        if source_img is None:
            st.write("No image is uploaded yet!")
        else:
            uploaded_image = PIL.Image.open(source_img)
            st.image(source_img, caption="Uploaded Image",
                        use_column_width=True)
    except Exception as ex:
        st.error("Error occurred while opening the image.")
        st.error(ex)

with col2:
    if source_img is None:
        st.write("Upload an image and click Detect!")
    else:
        if st.sidebar.button('Detect Objects'):
            res = model.predict(uploaded_image,
                                conf=confidence
                                )
            boxes = res[0].boxes
            res_plotted = res[0].plot()[:, :, ::-1]
            st.image(res_plotted, caption='Detected Image',
                        use_column_width=True)
            try:
                with st.expander("Detection Results"):
                    for box in boxes:
                        st.write(box.data)
            except Exception as ex:
                # st.write(ex)
                st.write("No image is uploaded yet!")



st.sidebar.link_button("Go to 📷 Image Viewer", "https://smart-farming-new-website-kvnzazxebld8rmbqn7wxtd.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌵 Weed Density Visualiser", "https://smart-farming-new-website-h5kwkh5khqgspsxyjbdtf5.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 💮 Yield Prediction Page", "https://smart-farming-new-website-g8gdqxh5ywzzxjuxlc24gj.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🟫 Soil Suitability Analysis Page", "https://smart-farming-new-website-bayd9vjj9rtayxfudzevka.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🍀☘️ Type-Wise Weed Distribution Page", "https://smart-farming-new-website-wmhu4udtinqlakhkuy6rqd.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌺 Cotton Bud Lifecycle Stage Distribution Page", "https://smart-farming-new-website-y9shrzmwa5cfbgljffkqqh.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🍂🐞Disease, Pest and Deficiency distribution Page", "https://smart-farming-new-website-sm7pqb6ikfh7puskq6ouvd.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🥦 Cotton Bud Counter and Visualiser Page", "https://smart-farming-new-website-5fq6gxmptymgxztjevghhq.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🌩️ Weather Page", "https://mausam.imd.gov.in/imd_latest/contents/satellite.php", use_container_width=True)
st.sidebar.link_button("Go to 🤖 Chat Bot App", "https://smart-farming-new-website-eqsnsbopemwhxcxpvf6zjc.streamlit.app/", use_container_width=True)
st.sidebar.link_button("Go to 🖥️ Main Page", "https://smart-farming-new-website-5fq6gxmptymgxztjevghhq.streamlit.app/", use_container_width=True)
