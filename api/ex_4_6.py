import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App title
st.title("📈 Matplotlib Line Graph in Streamlit")

# Generate random dataset
x = np.linspace(0, 10, 100)  # X-axis values
y = np.sin(x) + np.random.normal(scale=0.2, size=len(x))  # Y-axis values with noise

# Create Matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y, label="Random Data", color="b", linewidth=2)
ax.set_title("📊 Random Line Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Display the Matplotlib figure in Streamlit
st.pyplot(fig)
