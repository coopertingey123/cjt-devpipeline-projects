import sqlite3

connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

sql_1 = "SELECT name, price FROM Products WHERE make='Apple'"

def row_to_dict(sql_statement):

    list_of_dicts = []
    rows = cursor.execute(sql_statement).fetchall()
    split_statement = sql_statement.split()
    index_of_from = split_statement.index("from".upper())
    columns = split_statement[1:index_of_from]

    for item in rows:
        dict1 = {}
        dict1[columns[0]] = item[0]
        dict1[columns[1]] = item[1]
        list_of_dicts.append(dict1)

    return(list_of_dicts)

print(row_to_dict(sql_1))


