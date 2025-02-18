import streamlit as st

# App title
st.title("🎛️ Reactive Slider in Streamlit")

# Slider widget (value changes dynamically)
value = st.slider("Select a number:", min_value=0, max_value=100, value=50)

# Display selected value in real-time
st.write(f"🔢 Selected Value: **{value}**")
