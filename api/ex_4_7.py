import streamlit as st
import pandas as pd

# App title
st.title("📊 Interactive Data Table with Pandas")

# Load sample dataset
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 28],
        "Score": [85, 92, 78, 88, 95]
    })

df = load_data()

# Display the dataframe interactively
st.write("### 🏆 Data Table:")
st.dataframe(df, use_container_width=True)

# Add a checkbox to show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Allow user to filter by age
age_filter = st.slider("Filter by Age", min_value=df["Age"].min(), max_value=df["Age"].max(), value=df["Age"].max())
filtered_df = df[df["Age"] <= age_filter]

st.write(f"### 🔍 Filtered Data (Age ≤ {age_filter}):")
st.dataframe(filtered_df)
