import streamlit as st
import sqlite3

DB_FILE = "queue.db"

st.title("Queue Manager Console")

conn = sqlite3.connect(DB_FILE)
jobs = conn.execute("SELECT job_id, status FROM jobs").fetchall()

st.write("### Job Status")
for job in jobs:
    st.write(f"**Job ID:** {job[0]}, **Status:** {job[1]}")

resubmit_job = st.text_input("Enter Job ID to Resubmit")
if st.button("Resubmit"):
    conn.execute("UPDATE jobs SET status='pending', retry_count=0 WHERE job_id=?", (resubmit_job,))
    conn.commit()
    st.success(f"Job {resubmit_job} has been resubmitted!")

cancel_job = st.text_input("Enter Job ID to Cancel")
if st.button("Cancel"):
    conn.execute("UPDATE jobs SET status='unprocessable' WHERE job_id=?", (cancel_job,))
    conn.commit()
    st.error(f"Job {cancel_job} marked as unprocessable!")
