from Config.db_config import get_connection

def insert_student(stu_name,stu_age,stu_reg_no):
    connection=get_connection()
    if connection is None:
        return False, "Could Not connect to Database"
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO all_students (stu_name,stu_age,stu_reg_no) VALUES (%s,%s,%s)",(stu_name,stu_age,stu_reg_no))
        connection.commit()
    except Exception as e:
        connection.rollback()
        return False, str(e)
    finally:
        connection.close()