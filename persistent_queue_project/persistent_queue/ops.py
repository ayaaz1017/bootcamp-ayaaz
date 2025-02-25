import streamlit as st
from persistent_queue.queue_interface import PersistentQueueInterface
from persistent_queue.queue_sqlite import PersistentQSQLite  # Default implementation

# Initialize queue (Can be changed dynamically)
queue: PersistentQueueInterface = PersistentQSQLite()

# Streamlit UI Setup
st.set_page_config(page_title="Persistent Queue Ops", layout="wide")

st.title("📊 Persistent Queue Operations Dashboard")
st.write("Monitor the queue status, job processing history, and error cases.")

# Fetch job statistics
total_jobs = queue.get_total_jobs()
pending_jobs = queue.get_pending_jobs()
in_progress_jobs = queue.get_in_progress_jobs()
failed_jobs = queue.get_failed_jobs()
processed_jobs = queue.get_processed_jobs()

# Display Job Summary
st.subheader("Queue Summary")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("📋 Total Jobs", total_jobs)
col2.metric("⏳ Pending", pending_jobs)
col3.metric("🚀 In Progress", in_progress_jobs)
col4.metric("❌ Failed", failed_jobs)
col5.metric("✅ Processed", processed_jobs)

st.divider()

# Display Job Details
st.subheader("📌 Job Details")
filter_option = st.selectbox("Filter Jobs by Status", ["All", "Pending", "In Progress", "Failed", "Processed"])

if filter_option == "All":
    jobs = queue.get_all_jobs()
elif filter_option == "Pending":
    jobs = queue.get_jobs_by_status("pending")
elif filter_option == "In Progress":
    jobs = queue.get_jobs_by_status("in_progress")
elif filter_option == "Failed":
    jobs = queue.get_jobs_by_status("failed")
elif filter_option == "Processed":
    jobs = queue.get_jobs_by_status("processed")

if jobs:
    st.table(jobs)
else:
    st.info("No jobs found for the selected filter.")

st.divider()

# Display Failed Jobs Analysis
st.subheader("⚠️ Failed Jobs Analysis")
failed_jobs_list = queue.get_failed_jobs_list()

if failed_jobs_list:
    for job in failed_jobs_list:
        st.write(f"**Job ID:** {job['job_id']}")
        st.write(f"🔄 Retries: {job['retry_count']} / Max Retries: {queue.MAX_RETRIES}")
        st.write(f"📝 Last Error: {job['error_message']}")
        st.write("---")
else:
    st.success("No failed jobs detected.")

st.divider()

st.caption("Persistent Queue System - Operations Monitoring")
