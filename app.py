import streamlit as st
import numpy as np
from PIL import Image

# FUNGSI GRAYSCALE METHODS
def grayscale_averaging(img):
    return np.mean(img, axis=2).astype(np.uint8)

def grayscale_weighting(img):
    return (0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]).astype(np.uint8)

def grayscale_desaturation(img):
    max_val = np.max(img, axis=2)
    min_val = np.min(img, axis=2)
    return ((max_val + min_val) / 2).astype(np.uint8)

def grayscale_decomposition_min(img):
    return np.min(img, axis=2).astype(np.uint8)

def grayscale_decomposition_max(img):
    return np.max(img, axis=2).astype(np.uint8)

def grayscale_single_channel(img, channel):
    return img[:,:,channel]

# UI STREAMLIT
st.title("Konversi Citra RGB ke Grayscale")

source = st.radio("Pilih sumber gambar:", ["Upload Gambar", "Gunakan Contoh"])

image = None

if source == "Upload Gambar":
    uploaded_file = st.file_uploader("Upload gambar...", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

elif source == "Gunakan Contoh":
    image = Image.open("image1.jpg").convert("RGB")
    st.info("Menggunakan gambar contoh")

method = st.selectbox("Pilih metode grayscale:", [
    "Averaging",
    "Weighting",
    "Desaturation",
    "Decomposition (Min)",
    "Decomposition (Max)",
    "Single Channel (Red)",
    "Single Channel (Green)",
    "Single Channel (Blue)"
])

if image is not None:
    img_array = np.array(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Citra Asli")
        st.image(image, use_container_width=True)

    with st.spinner("Processing..."):
        if method == "Averaging":
            gray = grayscale_averaging(img_array)
        elif method == "Weighting":
            gray = grayscale_weighting(img_array)
        elif method == "Desaturation":
            gray = grayscale_desaturation(img_array)
        elif method == "Decomposition (Min)":
            gray = grayscale_decomposition_min(img_array)
        elif method == "Decomposition (Max)":
            gray = grayscale_decomposition_max(img_array)
        elif method == "Single Channel (Red)":
            gray = grayscale_single_channel(img_array, 0)
        elif method == "Single Channel (Green)":
            gray = grayscale_single_channel(img_array, 1)
        elif method == "Single Channel (Blue)":
            gray = grayscale_single_channel(img_array, 2)

    with col2:
        st.subheader("Hasil Grayscale")
        st.image(gray, use_container_width=True, channels="L")

    st.success(f"Konversi selesai menggunakan metode: {method}")

else:
    st.warning("Silakan pilih atau upload gambar terlebih dahulu.")