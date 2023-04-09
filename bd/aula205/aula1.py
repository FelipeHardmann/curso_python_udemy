import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

conn =  sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id integer primary key autoincrement,'
    'name text,'
    'weight real'
    ')'
)

# Criando valores
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (name, weight)'
#     'VALUES (?, ?)',
#     ['Joana', 4]
# )

sql = f'INSERT INTO {TABLE_NAME} (name, weight) \
    VALUES (?, ?)'

cursor.executemany(
    sql, 
    (
        ('Hardmann', 73), ('Jamilton', 79)
    )
)

# SQLite não possui Truncate
# sql_sequence deleta toda a sequência do sqlite que fica armazenada -> id

conn.commit()
# SQL

cursor.close()
conn.close()
