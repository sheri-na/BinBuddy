import streamlit as st

#page header
st.set_page_config(page_title="BinBuddy", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap');
    
    html, body, div, p {
        font-family: "Open Sans", sans-serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
        font-variation-settings:
        "wdth" 100;
    }
 
    .stApp, .stMainBlockContainer, .stAppViewContainer, .stSidebar{
        background: #f1efe7 !important;
    }

    img {
        display: block;
        margin: 0 auto;
        align: center;
        width: 100%;
        height: 100%;
        padding-bottom: 0px;
    }
    p, div, span {
        color: #17320b;
        text-align: center !important;
    }
    .headline {
        color: #226107 !important;
        font-weight: 800 !important;
        font-size: 33px !important;
    }
    
    .a.button,a.button:link,a.button:visited {
        background-color: #226107 !important;
        color: #fff !important;
        border-radius: 27px !important;
        padding: 11px 29px !important;
        font-size: 20.5px !important;
        font-weight: 50 !important;
        text-decoration: none;!important;
        display: inline-block !important;
        box-shadow: 0 6px 12px rgba(34, 97, 7, 0.2) !important;
        transition: all 0.3s ease !important;
        margin: 24px auto 0 auto !important;
}   a.button:hover{
    background-color: #fff !important;
    color: #226107 !important;
    border: 1px solid #226107 !important;
    border-radius: 27px !important;
     box-shadow: 0 0 0 3px #226107 inset, 0 6px 12px rgba(34, 97, 7, 0.3) !important;
    transform: translateY(-2px);
}
    </style>
    """,
    unsafe_allow_html=True,
)
#center layout
st.markdown('<div class="main">', unsafe_allow_html=True)
#homepage logo
st.image("img/Bin-2.svg", width=360)

#subheading
st.markdown('<p class="headline">Snap it. Sort it.</p>', unsafe_allow_html=True)

st.write("This app helps you navigate the world of recycling.")
st.write("Snap or upload a photo, and It'll tell you if it belongs in Recycle, Compost, or Trash.")

#button
st.markdown(
    """
    <a href="./sort_item" target="_self" class="button">Start Sorting</a>
    """,
    unsafe_allow_html=True
)


