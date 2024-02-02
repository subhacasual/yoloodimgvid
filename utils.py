
from io import BytesIO
import base64
from twilio.rest import Client
import streamlit as st
from PIL import Image
import numpy as np
import os


def get_image_download_link(img):

    """
    Generates a link allowing the PIL image to be downloaded
    in:  PIL image
    out: href string
    """
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download ="result.jpg">Download Image</a>'
    return href

# convert streamlit file buffer to nd array
def buffer2array(bufferfile):
    img = Image.open(bufferfile)
    return np.array(img)
  


@st.cache_data
def get_ice_servers():
    """
    Use Twilio's TURN server
    """

    # Ref: https://www.twilio.com/docs/stun-turn/api
    try:
        account_sid = 'AC90c93b83ff1a1634c360fff5c213aa77'
        auth_token = 'b74db5e477d51db800df128bce05bae9'
        # account_sid = os.environ['TWILIO_SID']
        # auth_token = os.environ['TWILIO_TOKEN']
        print("Twilo Authenticated Successful")
    except KeyError:
        print("Twilio credentials are not set. Fallback to a free STUN server from Google.")
        # logger.warning(
        #     "Twilio credentials are not set. Fallback to a free STUN server from Google."  # noqa: E501
        # )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    client = Client(account_sid, auth_token)

    token = client.tokens.create()
    print(token)
    return token.ice_servers
