import streamlit as st
from utils import buffer2array, get_image_download_link
from YOLOod.yolo_com_od import detect_objects

# @st.cache_data(experimental_allow_widgets=True)
def run_image_app():
    st.markdown('<h2 style="text-align: center; color: white;">Inference On Image</h2>', unsafe_allow_html=True)

    # if image is selected
    buffer = st.file_uploader("Upload an image 🎈 JPG Only", type=["jpg", "jpeg"])
    if buffer is not None:
        # st.image(buffer, caption="Uploaded Image", use_column_width=True)

        # coverting to np array
        image_array = buffer2array(buffer)

        # DO API CALLS HERE AND GET IMAGE BACK WITH BBOX PLOTTED
        # Demo API
        try:
            with st.spinner("Wait for API Response..."):
                result_image = detect_objects(image_array)
                if type(result_image) == str:
                    st.error(result_image)
                else:
                    st.image(result_image, caption="Result Image", use_column_width=True)
                    st.markdown(get_image_download_link(result_image), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"🤐😔 API is Down. Please come after some time. {e}")

    else:
        st.info("Please upload an image file")
        image_array = st.camera_input("Or use your camera to take a picture")
        if image_array is not None:
            # st.image(image_array, caption="Captured Image", use_column_width=True)
            # DO API CALLS HERE AND GET IMAGE BACK WITH BBOX PLOTTED
            # Demo API
            try:
                with st.spinner("Wait for API Response..."):
                    result_image = detect_objects(buffer2array(image_array))
                    if type(result_image) == str:
                        st.error(result_image)
                    else:
                        st.image(result_image, caption="Result Image", use_column_width=True)
                        st.markdown(get_image_download_link(result_image), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"🤐😔 API is Down. Please come after some time. {e}")

        else:
            st.info("Please take a picture or upload an image file")
    # print(buffer)