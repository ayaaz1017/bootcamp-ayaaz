import streamlit as st

# Dummy username and password (Replace with a secure method in production)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login Function
def login():
    st.title("🔒 Login Page")

    # Username & Password Input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login Button
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password.")

# Main App Function
def main_app():
    st.title("🎉 Welcome to the Secure App!")
    st.write("You have successfully logged in.")

    # Logout Button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()

# Show Login Page or Main App based on Authentication
if st.session_state.authenticated:
    main_app()
else:
    login()
