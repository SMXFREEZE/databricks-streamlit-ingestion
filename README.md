# Databricks Streamlit Data Ingestion App

A lightweight, serverless web application built to streamline data entry directly into a Databricks Data Lake.

## 🚀 Features
- **Frontend:** Built with Streamlit for a responsive, user-friendly interface.
- **Backend:** Connects to a Databricks SQL Warehouse (Serverless).
- **Storage:** Writes validated data directly to Delta Lake tables (ACID compliant).
- **Security:** Uses environment variables for credential management.

## 🛠️ Architecture
[Streamlit App] -> [Databricks SQL Connector] -> [Serverless Warehouse] -> [Delta Table]

## 📋 Prerequisites
- A Databricks Workspace
- A SQL Warehouse (Serverless or Pro)
- Python 3.8+

## 🔧 Setup
1. Clone the repo:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/databricks-streamlit-ingestion.git](https://github.com/YOUR_USERNAME/databricks-streamlit-ingestion.git)