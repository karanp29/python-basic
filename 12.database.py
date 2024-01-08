import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# --- CREATE TABLE
cursor.execute(
    """
    create table if not exists students (
               id integer primary key ,
               name text not null,
               age integer
    )
"""
)
if cursor:
    print("create success")
else:
    print("create fail")

# INSERT
name = "Karan"
age = 23
cursor.execute("INSERT INTO students (id,name, age) VALUES (?, ?, ?)", (2, name, age))
if cursor:
    print("insert success")
else:
    print("insert fail")

# SHOW - SELECT
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()
row_count = len(records)
print("row count is ", row_count)
for record in records:
    print(record)
