# Databricks Streamlit Ingestion

A lightweight, serverless application for secure data entry directly into Databricks Delta Lake.

## Overview

This project addresses a common engineering challenge: bridging the gap between manual user input and governed data storage. Instead of relying on shared spreadsheets or CSV uploads, this application provides a validated frontend that writes directly to a Delta table via a Serverless SQL Warehouse.

The goal was to create a solution that is low-maintenance, cost-effective (serverless), and secure by design.

## Architecture

The application follows a simple three-tier architecture:

1.  **Frontend:** Streamlit (Python) for the user interface and input validation.
2.  **Compute:** Databricks SQL Connector managing the connection to a Serverless SQL Warehouse.
3.  **Storage:** Delta Lake tables for ACID-compliant storage.

**Data Flow:**
User Input -> Parameterized SQL Query -> SQL Warehouse -> Delta Table

## Tech Stack

* **Python 3.x**
* **Streamlit:** For rapid UI development.
* **Databricks SQL Connector:** For Python-based SQL execution.
* **Pandas:** For result formatting and display.

## Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/databricks-streamlit-ingestion.git](https://github.com/YOUR_USERNAME/databricks-streamlit-ingestion.git)
cd databricks-streamlit-ingestion
