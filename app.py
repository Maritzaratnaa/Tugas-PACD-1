import streamlit as st
import numpy as np
from PIL import Image

def manual_rgb_to_gray(pixel_array):

    height, width, _ = pixel_array.shape
    
    # Canvas kosong untuk hasil grayscale (H, W)
    # Menggunakan dtype uint8 untuk standar warna 0-255
    gray_img = np.zeros((height, width), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            r = pixel_array[y, x, 0]
            g = pixel_array[y, x, 1]
            b = pixel_array[y, x, 2]
            
            # Algoritma Luminosity
            gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray_img[y, x] = gray_value
            
    return gray_img

# --- UI STREAMLIT ---
st.title("Konversi Citra: RGB ke Grayscale")

uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Membuka file untuk mendapatkan data array dasar
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Citra Asli (RGB)")
        st.image(image, use_container_width=True)
        
    # Proses Konversi
    with st.spinner("Mengonversi..."):
        gray_array = manual_rgb_to_gray(img_array)
    
    with col2:
        st.header("Hasil (Grayscale)")
        st.image(gray_array, use_container_width=True, channels="L")
        
    st.success("Konversi selesai menggunakan metode Luminosity!")