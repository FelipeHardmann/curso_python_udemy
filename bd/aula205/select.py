'''
    fetchall vai retorna todas as linhas do banco de dados
    fetchone irá retorna a primeira linha ou apenas uma linha do banco 
    fetchmany irá retornar uma lista
'''

import sqlite3

from aula1 import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    # Desempacotamento de Tupla
    # print(row)
    _id, name, weight = row
    print(_id, name, weight)


# for i in range(4):
#     print(cursor.fetchone)

cursor.close()
connection.close()
