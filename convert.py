#!/usr/bin/python
import sys

table_name = sys.argv[1] or 'my_table_name'
with open('default', 'r') as f:
    data = f.readlines()

query = 'INSERT INTO {table} ({columns}) VALUES {values};'

insert_data = {}

for each_data in data:
    if '*' in each_data:
        continue
    key, value = each_data.split(':', 1)
    key = key.strip()
    value = value.strip()
    if value == 'NULL':
        continue

    if key not in insert_data:
        insert_data[key] = []

    if not value.isdigit():
        # if there is `"` in the string, then use `'`
        if '"' in value:
            value = "'{}'".format(value)
        else:
            value = '"{}"'.format(value)
    insert_data[key].append(value)

# create column string
column_string = ', '.join(['`{}`'.format(key) for key, value in insert_data.items()])

value_map_to_rows = {}
for value in insert_data.values():
    for idx, column_value in enumerate(value):
        if idx not in value_map_to_rows:
            value_map_to_rows[idx] = []
        value_map_to_rows[idx].append(column_value)

row_string_list = []

for each_row in value_map_to_rows.values():
    each_row_string = '(' + ', '.join(each_row) + ')'
    row_string_list.append(each_row_string)

value_string = ', '.join(row_string_list)

query = query.format(table=table_name, columns=column_string, values=value_string)

print(query)
