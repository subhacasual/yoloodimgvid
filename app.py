import streamlit as st
from inference_page.image import run_image_app
from inference_page.video import run_video_app

# CSS Style code, copy IDs from broswer and then add properties.
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background: rgb(2,0,36);
background: linear-gradient(167deg, rgba(2,0,36,1) 0%, rgba(103,87,129,1) 60%, rgba(0,72,235,1) 100%);
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}


[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stFileUploadDropzone"]{{
    background-color: #3d2c5c;
    color: #ffffff;
    border: 0.2px solid #7d48d3;
}}

[data-testid="stCameraInputButton"] {{
    background-color: #7d48d3;
    transition: box-shadow 300ms ease-in-out,  color 300ms ease-in-out;
}}

[class="css-6qob1r e1akgbir3"] {{   
    background-color: #3d2c5c;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
hide_streamlit_style = """ <style>
#MainMenu {visibility: hidden;} 
#GithubIcon {visibility: hidden;}
footer {visibility: hidden;} 
</style> """ 
st.markdown(hide_streamlit_style, unsafe_allow_html=True) # Hides the Hamburger menu and footer


st.title("CoolR Model Inference App")

# # getting option for input types, image or video
# col1, col2 = st.columns(2)

# input_image = col1.checkbox("Inference on Image", help="Select this if you want to do inference on image")
# input_video = col2.checkbox("Inference on Video", help="Select this if you want to do inference on video")

input_type = st.radio(
    "Choose your Input type...",
    options=["Image 🖼️", "Live Feed 📽️"],
    horizontal=True)
    # captions = ["Select to run inferecne on image", "To run inference on live video."])

if input_type == "Image 🖼️":
    run_image_app()
else:
    run_video_app()
