dict1 = {
   'fields': [
      'name', 
      'model', 
      'price'
   ],
   'table': 'Products',
   'where': {
      'AND': [
      	 {
            'field': 'make',
            'value': '%Apple%',
            'operator': 'LIKE'
         },
         {
            'field': 'price',
            'value': 1100.00,
            'operator': 'lessthan'
         }
      ]
   },
   'order_by': {
      'field': 'price',
      'order': 'DESC'
   },
   'limit': 0
}

keys = dict1.keys()

def get_select():
    fields = dict1['fields']
    final_fields = ""
    for field in fields:
        final_fields = field + ", " + final_fields
    table = dict1['table']
    final_fields = final_fields[0:-2]
    select = f"SELECT {final_fields} FROM {table}"
    return select

# print(get_select())

def get_where():
    field = dict1['where']
    list_of_strings = []
    final_where_statement = "WHERE "
    if "AND" in field.keys():
        for dict in field["AND"]:
            list_of_strings.append(f"{dict['field']} {dict['operator']} {dict['value']}")
    else:
        list_of_strings.append(f"{field['field']} {field['operator']} {field['value']}")
    for i, list in enumerate(list_of_strings):
        if i == len(list_of_strings) - 1:
            final_where_statement = final_where_statement + list
            break
        final_where_statement = final_where_statement + list + " AND "
    return final_where_statement

# print(get_where())

def get_order():
    order_by = ""
    field = dict1['order_by']['field']
    order = dict1['order_by']['order']
    if "order_by" in keys:
        order_by = f"{field} {order}"
    return order_by


def get_limit():
    limit = ""
    limit1 = dict1['limit']
    if 'limit' in keys:
        limit = f"LIMIT {limit1}"
    return limit

def concat_all():
    select = get_select()
    where = get_where()
    order = get_order()
    limit = get_limit()
    return print(f"{select} {where} {order} {limit}")

# concat_all()


