# SQL Parser

var2 = "SELECT name, make, model, price FROM Products  WHERE price = 49.99 ORDER BY price DESC LIMIT 5;"
var3 = "SELECT first_name, last_name, email FROM Cohorts WHERE first_name = 'John'"
var4 = "SELECT city, state FROM Customers WHERE state = 'UT' ORDER BY city ASC"
var5 = "SELECT * FROM Courses ORDER BY name ASC LIMIT 20"
var1 = "SELECT * FROM Customers;"

def sql_parser(sql_string):
    dict1 = {
        'fields': [],
        'table': '',
        'where': {},
        'order by': {},
        'limit': 0
    }
    x = sql_string.split(' ')
    index_of_select = x.index("SELECT")
    index_of_from = x.index("FROM")

    if "WHERE" in x:
        index_of_where = x.index("WHERE")
    else:
        index_of_where = 0
    if "ORDER" in x:
        index_of_order_by = x.index("ORDER") + 1
    else:
        index_of_order_by = 0
    if "LIMIT" in x:
        index_of_limit = x.index("LIMIT")
    else:
        index_of_limit = 0

    dict1['fields'] = x[index_of_select+1 : index_of_from]
    dict1['table'] = x[index_of_from+1].strip(';')
    if index_of_where:
        dict1['where'] = {x[index_of_where+1] : x[index_of_where + 3].strip("'")}
    if index_of_order_by:
        dict1['order by'] = {'field': x[index_of_order_by+1], 'direction': x[index_of_order_by+2].strip(';')}
    if index_of_limit > 0:
        limit = x[index_of_limit+1].strip(';')
        dict1['limit'] = int(limit)
    return dict1
    
print(sql_parser(var2))