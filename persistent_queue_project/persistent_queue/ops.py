import streamlit as st
import sqlite3

DB_FILE = "queue.db"

st.title("Ops Console - Job Status")

conn = sqlite3.connect(DB_FILE)
jobs = conn.execute("SELECT job_id, status FROM jobs").fetchall()

st.write("### Job Status")
for job in jobs:
    st.write(f"**Job ID:** {job[0]}, **Status:** {job[1]}")
