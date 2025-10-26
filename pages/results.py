# pages/results.py
import io
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Sort Item – Results", layout="centered")

# ---------- Styles ----------
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

    .headline {
        color: #226107 !important;
        font-weight: 800 !important;
        font-size: 45px !important;
        text-align: center !important;
        margin-bottom: 0.2rem;
    }
    .pill {
        display: inline-block;
        padding: 0.8rem 1.4rem;
        border-radius: 999px;
        background: #ffffff;
        border: 1px solid #d3d0c7;
        font-weight: 600;              /* 580 -> 600 for consistency */
        font-size: 20px;
        color: #226107 !important;
        margin: 0.75rem auto 0.75rem auto;
    }

    p { font-size: 20px !important; }

    .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .stImage img {
        border-radius: 15px;
        display: block;
        margin: 0 auto;
    }

    a.button, a.button:link, a.button:visited {
        background-color: #226107 !important;
        color: #fff !important;
        border-radius: 27px !important;
        padding: 11px 29px !important;
        font-size: 20.5px !important;
        font-weight: 500 !important;
        text-decoration: none !important;
        display: inline-block !important;
        box-shadow: 0 6px 12px rgba(34, 97, 7, 0.2) !important;
        transition: all 0.3s ease !important;
        margin: 24px auto 0 auto !important;
    }
    a.button:hover {
        background-color: #fff !important;
        color: #226107 !important;
        border: 1px solid #226107 !important;
        border-radius: 27px !important;
        box-shadow: 0 0 0 3px #226107 inset, 0 6px 12px rgba(34, 97, 7, 0.3) !important;
        transform: translateY(-2px);
    }
    [data-testid="stSpinnerText"] {
        font-size: 30px !important;      
        font-weight: 500 !important;     
        color: #226107 !important;     
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<p class="headline">Result</p>', unsafe_allow_html=True)

#load image
ss = st.session_state
if "result_img_bytes" not in ss:
    st.warning("No image found. Please upload or take a picture first.")
    st.page_link("pages/sort_item.py", label="← Go to Sort Item")
    st.stop()

img_bytes = ss["result_img_bytes"]

try:
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    st.image(img, use_container_width=True)
except Exception as e:
    st.error(f"Could not display image: {e}")
    st.page_link("pages/sort_item.py", label="← Try again")
    st.stop()

#classification
try:
    import torch

    @st.cache_resource(show_spinner=False)
    def load_openclip():
        import open_clip
        model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32", pretrained="openai")
        tokenizer = open_clip.get_tokenizer("ViT-B-32")
        model.eval()
        return model, preprocess, tokenizer

    model, preprocess, tokenizer = load_openclip()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    CLASSES = ["recycle", "trash", "compost"]
    PROMPTS = [
        "a photo of an item that belongs in the recycling bin",
        "a photo of an item that belongs in the trash bin",
        "a photo of an item that belongs in the compost bin",
    ]

    @torch.no_grad()
    def classify_label(image_pil: Image.Image) -> str:
        image = preprocess(image_pil).unsqueeze(0).to(device)
        text_tokens = tokenizer(PROMPTS).to(device)
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_tokens)
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        text_features = text_features / text_features.norm(dim=-1, keepdim=True)
        logits = 100.0 * image_features @ text_features.T
        idx = int(logits.argmax(dim=-1).item())
        return CLASSES[idx]

    with st.spinner("Analyzing…"):
        label = classify_label(img)

    st.markdown(
        f"""
        <div>
          <span class="pill">Recommendation: {label.title()}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    def tip_for(lbl: str) -> str:
        if lbl == "recycle":
            return "Tip: Rinse if needed and check local rules (plastic codes, clean paper/cardboard)."
        if lbl == "compost":
            return "Tip: Remove plastic/metal; compost only food scraps and certified compostables."
        return "Tip: If it’s mixed material or contaminated, trash is safer to avoid recycling contamination."

    st.write(tip_for(label))

except ModuleNotFoundError:
    st.error(
        "Missing dependency for classification.\n\n"
        "Please install:\n"
        "`pip install torch torchvision torchaudio open-clip-torch`"
    )
    st.page_link("pages/sort_item.py", label="← Back to Sort Item")
    st.stop()
except Exception as e:
    st.error(f"Classification error: {e}")
    st.page_link("pages/sort_item.py", label="← Back to Sort Item")
    st.stop()

#try another
st.markdown(
    """
    <a href="http://localhost:8501/sort_item" target="_self" class="button">Try another</a>
    """,
    unsafe_allow_html=True,
)