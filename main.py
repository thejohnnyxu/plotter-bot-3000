import streamlit as st
from generators import noise_field, noise_preview, contours
from matplotlib import pyplot as plt

st.title("plotter-bot-3000")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Controls")
    size = st.number_input("Size", min_value=0, max_value=999, value=69)
    seed = st.number_input("Seed", min_value=0, max_value=999, value=42)
    levels = st.slider("Contour Levels", min_value=5, max_value=40, value=18)
    scale = st.slider("Scale", min_value=20, max_value=150, value=60)

field = noise_field.generate_noise_field(size, size, scale, seed) 
fig, ax = plt.subplots()
for contour in contours.generate_contours(field, levels):
    ax.plot(contour[:,1], contour[:,0])  # x coords, y coords


with col2:
    st.header("Preview")
    st.image(noise_preview.noise_to_image(noise_field.generate_noise_field(size, size, scale, seed)), caption="image preview")
    st.pyplot(fig)
    st.write(f"size: {size}")
    st.write(f"Seed: {seed}")
    st.write(f"Levels: {levels}")
    st.write(f"Scale: {scale}")    
    
