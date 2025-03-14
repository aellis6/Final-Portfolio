import streamlit as st
import info
import pandas as pd

# Homepage

def Home_Page():
    st.header("Home Page")
    st.image("images/welcome.gif", caption="Big welcome to recruiters--I'm looking for an internship!", use_container_width=True)
    st.write(info.welcome)
    for title, description in info.page_descriptions.items():
        st.markdown(f"<b>{title}</b>", unsafe_allow_html=True)
        st.write(description)

    st.write('---')
#NEW
if "green_mode" not in st.session_state:
    st.session_state["green_mode"] = False

button_style = """
    <style>
        div.stButton > button {
            background-color: #013220;
            color: white;
            border-radius: 10px;
            border: 2px solid #4eace4;
            padding: 10px 20px;
            font-size: 16px;
        }
        div.stButton > button:hover {
            background-color: #4eace4;
            color: white;
        }
    </style>
"""

st.markdown(button_style, unsafe_allow_html=True)

if st.button("Toggle Fun Mode"):
    st.session_state["green_mode"] = not st.session_state["green_mode"]

if st.session_state["green_mode"]:
    st.write("Fun mode is on")
    st.markdown("""
        <style>
            .stApp {
                background-color: #8fbc8f;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)


Home_Page()
# import streamlit as st
# import info
# import pandas as pd


# Homepage
# def Home_Page():
#     st.header("Home Page")
#     st.image(info.profile_picture, width = 200)
#     st.write(info.welcome)
#     st.write(info.page_descriptions)
#     st.write('---')

# if "dark_mode" not in st.session_state:
#     st.session_state["dark_mode"] = False

# if st.button("Toggle Dark Mode"):
#     st.session_state["dark_mode"] = not st.session_state["dark_mode"]

# if st.session_state["dark_mode"]:
#     st.write("Dark mode is on")
#     st.markdown("""
#                 <style>
#                     body{color-background: #1e1e1e; :white[body];}
#                 </style>
#                 """,
#                 unsafe_allow_html=True)

# Home_Page()