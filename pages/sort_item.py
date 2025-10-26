import io
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Sort Item", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');
    html, body, div, p {
        font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, sans-serif !important;
    }
    .stApp, .stAppViewContainer, .stMainBlockContainer, .stSidebar {
        background: #f1efe7 !important;
    }
   div[data-testid="stMarkdownContainer"] p.text {
        color: #17320b  !important;
        text-align: center !important;
        font-size: 19px !important;
        line-height: 1.3;
        margin-top: 0.5em;
}
    .headline {
        color: #226107 !important;
        font-weight: 800 !important;
        font-size: 45px !important;
        text-align: center !important;
    }
 
    /* Center the uploader and camera blocks themselves */
    div[data-testid="stFileUploader"],
    div[data-testid="stCameraInput"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;   /* centers horizontally */
        justify-content: center !important;
        text-align: center !important;
        width: 99%;
}
    /* Style and center the inner label text */
    div[data-testid="stFileUploader"] label,
    div[data-testid="stCameraInput"] label,
    div[data-testid="stFileUploader"] label :is(p, span, div),
    div[data-testid="stCameraInput"] label :is(p, span, div) {
        font-size: 19px !important;
        font-weight: 200 !important;
        color: #17320b !important;
        text-align: center !important;
        width: 100%;
}

    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="headline">Sort Item</p>', unsafe_allow_html=True)
st.markdown('<p class="text">Snap or upload a photo, then It’ll suggest the correct bin.</p>', unsafe_allow_html=True)

upload = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if upload is not None:
    img_bytes = upload.getvalue()
    st.image(img_bytes, caption='Uploaded Image', use_container_width=True)
    try:
        img = Image.open(io.BytesIO(img_bytes))
        st.write("Image successfully uploaded.")

        st.session_state["result_img_bytes"] = img_bytes
        st.session_state["source"] = "upload"
        st.switch_page("pages/results.py")

    except Exception as e:
        st.error(f"An error occurred loading image: {e}")

picture = st.camera_input("Take a photo")

if picture is not None:
    try:
        cam_bytes = picture.getvalue()
        _ = Image.open(io.BytesIO(cam_bytes)).convert("RGB")

        st.session_state["result_img_bytes"] = cam_bytes
        st.session_state["source"] = "camera"
        st.switch_page("pages/results.py")

    except Exception as e:
        st.error(f"An error occurred with the camera image: {e}")

