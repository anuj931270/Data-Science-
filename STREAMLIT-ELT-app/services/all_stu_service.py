from Config.db_config import get_connection

def get_all_students():
    connection=get_connection()
    if connection is None:
        return False, "Could not connect to database"
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM all_students")
            return cursor.fetchall()
    except Exception as e:
        return False, str(e)
    finally:
        connection.close()