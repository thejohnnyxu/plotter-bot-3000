import streamlit as st

st.title("plotter-bot-3000")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Controls")
    seed = st.number_input("Seed", min_value=0, max_value=999, value=42)
    levels = st.slider("Contour Levels", min_value=5, max_value=40, value=18)
    scale = st.slider("Scale", min_value=20, max_value=150, value=60)

with col2:
    st.header("Preview")
    st.write(f"Seed: {seed}")
    st.write(f"Levels: {levels}")
    st.write(f"Scale: {scale}")