import sqlite3
connection = sqlite3.connect("hospitals.db")
cursor = connection.cursor()

# with open("sql_create_table.sql") as sql_file:
#     sql_as_string = sql_file.read()
#     cursor.executescript(sql_as_string)

with open("get_data.sql") as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

connection.commit()  