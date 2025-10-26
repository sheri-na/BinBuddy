import streamlit as st

#page header
st.set_page_config(page_title="BinBuddy", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&display=swap');

    html, body, [class*="st-"], div, p, span {
        font-family: 'Courier Prime', monospace !important;
    }
    .stApp, .stMainBlockContainer, .stAppViewContainer, .stSidebar{
        background: #f1efe7 !important;
    }

    img {
        display: block;
        margin: 0 auto;
        padding: 0 auto;
        align: center;
    }
    p, div, span {
        color: #17320b;
        text-align: center !important;
    }
    .headline {
        color: #226107 !important;
        font-weight: 100 !important;
        font-size: 27px !important;

    }
    </style>
    """,
    unsafe_allow_html=True,
)
#center layout
st.markdown('<div class="main">', unsafe_allow_html=True)
#homepage logo
st.image("img/Bin.svg", width=393)

#subheading
st.markdown('<p class="headline">Snap it. Sort it.</p>', unsafe_allow_html=True)


st.write("This app helps you navigate the world of recycling.")
st.write("Snap or upload a photo, and I'll tell you if it belongs in Recycle, Compost, or Trash.")
st.write("Start Sorting")