import streamlit as st
from pyaxidraw import axidraw
from matplotlib import pyplot as plt

# Page Title
st.title("Command Center")

# Cookies (session states)
if "ad" not in st.session_state:
    st.session_state.ad = axidraw.AxiDraw()

if "current_location" not in st.session_state:
    st.session_state.current_location = (0.0,0.0)

if "movement_history" not in st.session_state:
    st.session_state.movement_history = [(0.0,0.0)]

# sets the ridiculous session state object name and make it "ad" again
ad = st.session_state.ad
current_location = st.session_state.current_location
movement_history = st.session_state.movement_history

# ------ LAYOUT -------
with st.container():
    st.header("Device:")
    
    plotter_connected = st.toggle("Connect")
    
    try:
        if plotter_connected:
            ad.interactive()
            ad.connect()
        else:
            ad.disconnect()
    except Exception as e:
        st.error(e)

outer_col1, outer_col2 = st.columns([1,1])

with outer_col2:
    with st.container():
        st.header("Pen Controls:")
        if st.button("Raise"):
                ad.penup()
        if st.button("Lower"):
            ad.pendown()

    with st.container():
        st.header("Carriage Controls:")    
        st.subheader("Movement Scale")
        magnitude = st.slider("Movement Scale", 0.01, 1.0 )

        st.subheader("Controls")
        col1, col2, col3  = st.columns([1,1,1])

        with col2:
            if st.button("Return Home"):
                ad.moveto(0,0)
                current_location = (0.0,0.0)
                st.session_state.current_location = current_location
                movement_history.clear()
                movement_history.append((0,0))
            
            if st.button("Up"):
                ad.go(0, -magnitude)
                current_location = (current_location[0], current_location[1] + -magnitude)
                st.session_state.current_location = current_location
                movement_history.append(current_location)
                #st.write(f'{current_location}, {movement_history}')

            if st.button("Down"):
                ad.go(0, magnitude)
                current_location = (current_location[0], current_location[1] + magnitude)
                st.session_state.current_location = current_location
                movement_history.append(current_location)
                #st.write(f'{current_location}, {movement_history}')
        
        with col1:
            st.space()
            if st.button("Left"):
                ad.go(-magnitude, 0)
                current_location = (current_location[0] + -magnitude, current_location[1])
                st.session_state.current_location = current_location
                movement_history.append(current_location)
                #st.write(f'{current_location}, {movement_history}')

        with col3:
            st.space()
            if st.button("Right"):
                ad.go(magnitude, 0)
                current_location = (current_location[0] + magnitude, current_location[1])
                st.session_state.current_location = current_location
                movement_history.append(current_location)
                #st.write(f'{current_location}, {movement_history}')

with st.container():
        st.header("Minimap")
        # Setting up the plotting values from the noise and contours
        fig, ax = plt.subplots(figsize=(11,8.5))
        ax.yaxis.set_inverted(True)
        ax.set_xlim(0, 11)
        ax.set_ylim(8.5, 0)
        xs, ys = zip(*movement_history)
        
        # Plotting
        ax.plot(xs, ys)
        print(fig.get_figwidth(), fig.get_figheight(), ax.get_xlim(), ax.get_ylim())

        st.pyplot(fig, width="content")


# with outer_col1: 
#     with st.container():
#         st.header("Minimap")
#         # Setting up the plotting values from the noise and contours
#         fig, ax = plt.subplots(figsize=(6,4.6))
#         ax.yaxis.set_inverted(True)
#         ax.set_xlim(0, 11)
#         ax.set_ylim(8.5, 0)
#         xs, ys = zip(*movement_history)
#         ax.plot(xs, ys)
#         st.pyplot(fig, width="content")
#         print(fig.get_size_inches())


# col1, col2 = st.columns([1, 1])
# with col1:

#     st.header("Utlity Actions:")
#     if st.button("Quick Test"):                        # Absolute moves follow:
#         ad.moveto(1, 1)                 # Pen-up move to (1 inch, 1 inch)
#         ad.lineto(2, 1)                 # Pen-down move, to (2 inch, 1 inch)
#         ad.moveto(0, 0)                 # Pen-up move, back to origin.
    
#     if st.button("Disable Motors"):
#         ad.plot_setup()
#         ad.options.mode = "manual"
#         ad.options.manual_cmd = "disable_xy"
#         ad.plot_run()
    
#     if st.button("Enable Motors"):
#         ad.plot_setup()
#         ad.options.mode = "manual"
#         ad.options.manual_cmd = "enable_xy"
#         ad.plot_run()

#     if st.button("Return Home"):
#         ad.moveto(0,0)
#         current_location = (0.0,0.0)
#         movement_history.clear()
#         movement_history.append((0,0))



# with col2:
#     with st.container():
#         st.header("Pen Controls:")
#         if st.button("Raise"):
#                 ad.penup()
#         if st.button("Lower"):
#             ad.pendown()

#     with st.container():
#         st.header("Carriage Controls:")    
#         st.subheader("Movement Scale")
#         magnitude = st.slider("Movement Scale", 0.01, 1.0 )

#         st.subheader("Controls")
#         col1, col2, col3  = st.columns([1,1,1])

#         with col2:
#             if st.button("Up"):
#                 ad.go(0, -magnitude)
#                 current_location = current_location + (0, -magnitude) 
#                 movement_history.append((0.0, -magnitude))
#                 st.write(f'{current_location}, {movement_history}')

#             if st.button("Down"):
#                 ad.go(0, magnitude)
#                 current_location = current_location + (0, magnitude)
#                 movement_history.append((0.0, magnitude))
#                 st.write(f'{current_location}, {movement_history}')
        
#         with col1:
#             st.space()
#             if st.button("Left"):
#                 ad.go(-magnitude, 0)
#                 current_location = current_location + (-magnitude, 0)
#                 movement_history.append((-magnitude, 0))
#                 st.write(f'{current_location}, {movement_history}')

#         with col3:
#             st.space()
#             if st.button("Right"):
#                 ad.go(magnitude, 0)
#                 current_location = current_location + (magnitude, 0)
#                 movement_history.append((magnitude, 0))
#                 st.write(f'{current_location}, {movement_history}')

        
