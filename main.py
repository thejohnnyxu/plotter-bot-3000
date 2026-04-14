import streamlit as st

st.title("plotter-bot-3000")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Controls")
    seed = st.number_input("Seed", min_value=0, max_value=999, value=42)
    levels = st.slider("Contour Levels", min_value=5, max_value=40, value=18)
    scale = st.slider("Scale", min_value=20, max_value=150, value=60)
    vibe = st.text_input("Vibe", value="Put whatever text you want in here and it will be used to generate the plot. The more words you use, the more complex the plot will be. You can also use emojis! 🎨✨")
    
    ## I think that "if st.button()" means that if I click the button, then the following happens. So in this case, if I click the button, then it will display the vibe that I entered in the text input.
    if st.button("Tell me the vibe!"):
        st.info(f"{vibe} and seed: {seed} and levels: {levels} and scale: {scale}")

with col2:
    st.header("Preview")
    st.write(f"Seed: {seed}")
    st.write(f"Levels: {levels}")
    st.write(f"Scale: {scale}")    
