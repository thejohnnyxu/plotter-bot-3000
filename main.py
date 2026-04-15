from rich import traceback
traceback.install()
import streamlit as st
from generators import noise_field, noise_preview, contours
from matplotlib import pyplot as plt

st.title("🤖 Plotter Bot 3000")

##### Testing on my own

#levanzo colors
paper = "#EEE8DC"
ink = "#E4D8C0"

# left nav
favicon = "images/levanzo-16.svg"
small_logo_sidebar = "images/levanzo-32.svg"
large_logo_sidebar = "images/levanzo-64.svg"
small_logo_main = "images/levanzo-128.svg"
large_logo_main = "images/levanzo-200.svg"

# Main app from lessons
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Controls")
    size = st.number_input("Size", min_value=0, max_value=999, value=69)
    seed = st.number_input("Seed", min_value=0, max_value=999, value=42)
    levels = st.slider("Contour Levels", min_value=5, max_value=40, value=18)
    scale = st.slider("Scale", min_value=20, max_value=150, value=60)

# Setting up the plotting values from the noise and contours
field = noise_field.generate_noise_field(size, size, scale, seed) 
fig, ax = plt.subplots()
# added .set_axis_off()
# can also use ax.axis("off")
ax.set_axis_off()
# set fig and ax color to black, facecolor seems to be bg color
# why did we need to set ax color if we disabled it
fig.set_facecolor("black")
ax.set_facecolor("black")

# field is not from matplotlib, it just has an array of numbers from numpy
# fig and ax are matplotlib, they are being set to plt.subplots() (how can it be both?)
# contours are also a numpy thing, turning numbers in the field and smoothing and connecting them to make contour lines
# we are plotting each point in the contours array (how does it smooth the lines and make curves?)

# the color is applied when we plot
for contour in contours.generate_contours(field, levels):
    ax.plot(contour[:,1], contour[:,0], color=ink)  # x coords, y coords


with col2:
    st.header("Preview")
    st.image(noise_preview.noise_to_image(noise_field.generate_noise_field(size, size, scale, seed)), caption="image preview")
    st.pyplot(fig)
    st.write(f"size: {size}")
    st.write(f"Seed: {seed}")
    st.write(f"Levels: {levels}")
    st.write(f"Scale: {scale}")    
    
