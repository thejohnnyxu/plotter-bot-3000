import streamlit as st
from pyaxidraw import axidraw

# Page Title
st.title("Command Center")

# Cookies (session states)
if "ad" not in st.session_state:
    st.session_state.ad = axidraw.AxiDraw()
# sets the ridiculous session state object name and make it "ad" again
ad = st.session_state.ad

# ------ LAYOUT -------
col1, col2 = st.columns([1, 1])

with col1:
    # Connect
    try:
        if st.button("Connect"):
            ad.interactive()
            ad.connect()
            st.success("Connected to plotter...")
    except Exception as e:
        st.error(e)
        
    # Disconnect
    if st.button("Terminate"):
        st.toast("Terminated!!!")
        ad.disconnect()

    if st.button("Quick Test"):                        # Absolute moves follow:
        ad.moveto(1, 1)                 # Pen-up move to (1 inch, 1 inch)
        ad.lineto(2, 1)                 # Pen-down move, to (2 inch, 1 inch)
        ad.moveto(0, 0)                 # Pen-up move, back to origin.


with col2:
    try:
        if st.button("Up Pen"):
            ad.penup()
            st.success("Raised Pen")
    except Exception as e:
        st.error(e)
    

    if st.button("Down Pen"):
        ad.pendown()
        st.toast("Moved down")

        
    if st.button("Left"):
        ad.go(-0.05, 0)

    if st.button("Right"):
        ad.go(0.05, 0)

    if st.button("Up"):
        ad.go(0, -.05)

    if st.button("Down"):
        ad.go(0, .05)
