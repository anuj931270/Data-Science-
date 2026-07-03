# Step	What happens
# Extract	Order data comes from website
# Transform	Clean + calculate totals + validate
# Load	Save into database for reports

import pymysql
import json
import os
print("Current Working Directory:", os.getcwd())

# =========================
# STEP 1: LOAD JSON FILES
# =========================

with open("table.json", "r") as f:
    schema = json.load(f)

with open("student_profile.json", "r") as f:
    student_schema = json.load(f)


# =========================
# STEP 2: DB CONNECTION
# =========================

mysql_db = pymysql.connect(
    host="localhost",
    user="root",
    password="Root"
)

cursor = mysql_db.cursor()


# =========================
# STEP 3: CREATE DATABASE
# =========================

db_name = schema["database"]

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cursor.execute(f"USE {db_name}")

print(f"Database '{db_name}' ready.")


# =========================
# STEP 4: CREATE TABLE
# =========================

col_definition = ",".join(
    [f"{col} {dtype}" for col, dtype in schema["columns"].items()]
)

table_name = schema["table_name"]

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {table_name} ({col_definition})"
)

print(f"Table '{table_name}' created.")


# =========================
# STEP 5: INSERT DATA
# =========================

students = student_schema["students"]

for student in students:

    sql = f"""
        INSERT INTO {table_name}
        (first_name, age, email, phone, role)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        student["first_name"],
        student["age"],
        student["email"],
        student["phone"],
        student["role"]
    )

    cursor.execute(sql, values)


# =========================
# STEP 6: COMMIT & CLOSE
# =========================

mysql_db.commit()

print(f"{len(students)} records inserted successfully!")

cursor.close()
mysql_db.close()