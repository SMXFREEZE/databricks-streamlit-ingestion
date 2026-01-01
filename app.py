import streamlit as st
from databricks import sql
import pandas as pd
import os

# ==========================================
# CONFIGURATION
# Secrets are managed via Environment Variables for security
# ==========================================
SERVER_HOSTNAME = os.getenv("DATABRICKS_HOST", "your-server-hostname-here")
HTTP_PATH       = os.getenv("DATABRICKS_HTTP_PATH", "your-http-path-here")
ACCESS_TOKEN    = os.getenv("DATABRICKS_TOKEN", "your-access-token-here")

# 1. DATABASE CONNECTION
def run_query(query, params=None):
    try:
        with sql.connect(server_hostname=SERVER_HOSTNAME, http_path=HTTP_PATH, access_token=ACCESS_TOKEN) as conn:
            with conn.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                if query.strip().upper().startswith("SELECT"):
                    columns = [desc[0] for desc in cursor.description]
                    return cursor.fetchall(), columns
                return None, None
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return None, None

# 2. PAGE LAYOUT
st.title("Data Entry: A, B, C")
st.write("Use this form to add new data to the warehouse.")

# 3. INITIALIZE TABLE
try:
    run_query("""
        CREATE TABLE IF NOT EXISTS default.inputs (
            id BIGINT GENERATED ALWAYS AS IDENTITY,
            space_a STRING, 
            space_b STRING, 
            space_c STRING
        )
    """)
except Exception as e:
    st.error(f"Setup Error: {e}")

# 4. THE INPUT FORM
with st.form("entry_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        a = st.text_input("Space A")
    with c2:
        b = st.text_input("Space B")
    with c3:
        c = st.text_input("Space C")
        
    submitted = st.form_submit_button("Save to Database")

    if submitted:
        if a and b and c:
            run_query(
                "INSERT INTO default.inputs (space_a, space_b, space_c) VALUES (?, ?, ?)",
                (a, b, c)
            )
            st.success(f"Saved: {a}, {b}, {c}")
        else:
            st.warning("Please fill in all three spaces.")

# 5. SHOW SAVED DATA
st.divider()
st.subheader("Recent Entries")
try:
    rows, columns = run_query("SELECT * FROM default.inputs ORDER BY id DESC LIMIT 5")
    if rows:
        st.table(pd.DataFrame(rows, columns=columns))
    else:
        st.info("No data found yet.")
except Exception as e:
    st.error(f"Could not load data: {e}")