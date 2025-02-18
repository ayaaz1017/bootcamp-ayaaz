import streamlit as st
from streamlit_option_menu import option_menu
import pages.home as home
import pages.about as about

# Set up the sidebar navigation
st.sidebar.title("Navigation")
page = option_menu(
    menu_title=None,
    options=["Home", "About"],
    icons=["house", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

# Load the selected page
if page == "Home":
    home.show()
elif page == "About":
    about.show()
