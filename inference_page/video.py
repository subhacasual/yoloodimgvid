import streamlit as st
from streamlit_webrtc import webrtc_streamer
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av
from utils import get_ice_servers
from YOLOod.yolo_com_od import detect_objects

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")
        # print(image.shape)
        # print(type(image))
        # result_frame = detect_objects(image)
        result_frame = detect_objects(image)
                
        return av.VideoFrame.from_ndarray(result_frame, format="bgr24")

def run_video_app():
    st.markdown('<h2 style="text-align: center; color: white;">Inference On Video</h2>', unsafe_allow_html=True)

    # webrtc_streamer(key="sample",
    #                 video_frame_callback=video_frame_callback,
    #                 mode=WebRtcMode.SENDRECV,
    #                 rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    #                 # media_stream_constraints={"video": True, "audio": False},
    #                 async_processing=True)

    webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": get_ice_servers()},
        video_frame_callback=video_frame_callback,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )