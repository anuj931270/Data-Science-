import streamlit as st
from Config.db_config import check_health
from services.registration_service import insert_student
from services.all_stu_service import get_all_students


st.set_page_config(page_title="Student Management System",layout="wide")
st.title("📚 Student Management System")

health=check_health()

if health["status"]=="healthy":
    st.success(f"✅ {health['detail']}")
else:
    st.error(f"❌ {health['detail']}")
    st.stop()

st.write("Welcome ! 🌐")

col1,col2=st.columns(2)

#Left Columns 
with col1:
    st.header("📝Register Student")

    with st.form("stu_reg_form",clear_on_submit=True):
        stu_name=st.text_input("Student Name")
        stu_age=st.number_input("Student Age", min_value=1, max_value=100, value=None)
        stu_reg_no=st.text_input("Registation No")

        submmited=st.form_submit_button("Register Now",use_container_width=True)
        if submmited:
            try:
                success= insert_student(stu_name.strip(),int(stu_age),stu_reg_no.strip())
                if success:
                    st.success(f"✅ {stu_name} Registered suceessfully")
            except Exception as e:
                st.error(f"Error:{e}")


#right column

with col2:
    st.subheader("📂Register Student")

    try:
        students=get_all_students()

        if students:
            st.dataframe(students,width="stretch",hide_index=True)
        else:
            st.info("No Student Registered yet")
    except Exception as e:
        st.error(f"Could no load student {e}")