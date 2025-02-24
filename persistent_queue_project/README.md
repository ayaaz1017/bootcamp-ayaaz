# Persistent Queue System

## Overview
A producer-consumer system where:
- **Producers** submit jobs to a **persistent queue**.
- **Consumers** process jobs and ensure data integrity.
- **Ops Console** allows monitoring job status.
- **Admin Console** enables resubmitting/canceling jobs.

## Setup
1. Install dependencies:
   ```sh
   pip install streamlit sqlite3 supervisor
