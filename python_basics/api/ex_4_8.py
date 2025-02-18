import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# App title
st.title("📊 Interactive Plotly Scatter Plot in Streamlit")

# Generate a random dataset
@st.cache_data
def generate_data(n=100):
    np.random.seed(42)
    return pd.DataFrame({
        "X": np.random.rand(n) * 100,
        "Y": np.random.rand(n) * 100,
        "Category": np.random.choice(["A", "B", "C"], size=n)
    })

df = generate_data()

# Sidebar controls
st.sidebar.header("Scatter Plot Controls")
category_filter = st.sidebar.multiselect("Select Category:", options=df["Category"].unique(), default=df["Category"].unique())

# Filter data based on selection
filtered_df = df[df["Category"].isin(category_filter)]

# Create Plotly scatter plot
fig = px.scatter(filtered_df, x="X", y="Y", color="Category", title="Interactive Scatter Plot")

# Display the Plotly figure in Streamlit
st.plotly_chart(fig, use_container_width=True)
