import streamlit as st
from Config.db_config import check_health

st.set_page_config(page_title="Student Management System",layout="wide")
st.title("📚 Student Management System")

health=check_health()

if health["status"]=="healthy":
    st.success(f"✅ {health['detail']}")
else:
    st.error(f"❌ {health['detail']}")
    st.stop()

st.write("Welcome ! 🌐")