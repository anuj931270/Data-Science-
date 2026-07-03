import pymysql
import json


# STEP 1 : File Fetch
with open("table.json") as f:
    schema = json.load(f)

with open("student_profile.json") as f:
    student_schema = json.load(f)

# STEP 2 : DB CONNECTION
mysql_db=pymysql.connect(
    host="localhost",
    user="root",
    password="root@123"
)

cursor=mysql_db.cursor()

# STEP 3 : DB CREATION AND USE
db_name=schema['database']
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

print(F"DATABASE : {db_name} is ready to use ." )
cursor.execute(F"USE {db_name}")

col_defination=",".join([f"{col} {dtype}" for col,dtype in schema["columns"].items()])
cursor.execute(f"CREATE TABLE IF NOT EXISTS {schema["table_name"]} ({col_defination})")
print("Table create using json schema")

# STEP:4 
row_defination=student_schema["students"]
print(row_defination)

mysql_db.commit()
cursor.close()
mysql_db.close()