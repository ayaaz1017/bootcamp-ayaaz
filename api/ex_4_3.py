import streamlit as st

# Initialize session state for counter if not present
if "count" not in st.session_state:
    st.session_state.count = 0

# Display Counter
st.title("🔢 Counter App with Session State")
st.write(f"Current Count: **{st.session_state.count}**")

# Increment Button
if st.button("➕ Increment"):
    st.session_state.count += 1
    st.experimental_rerun()

# Decrement Button (Optional)
if st.button("➖ Decrement"):
    st.session_state.count -= 1
    st.experimental_rerun()

# Reset Button
if st.button("🔄 Reset"):
    st.session_state.count = 0
    st.experimental_rerun()
