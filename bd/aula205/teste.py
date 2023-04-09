import sqlite3

from aula1 import DB_FILE, TABLE_NAME

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight)

# row = cursor.fetchone()
# _id, name, weight = row

# print(_id, name, weight)

row = cursor.fetchmany()

print(row)
