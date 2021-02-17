import sqlite3

conexao = sqlite3.connect('DB.db')
cursor = conexao.cursor()
"""
cursor.execute(
    'create table if not exists users(              '
    'ID_USER integer primary key autoincrement,     '
    'NAME_USER text not null,                       '
    'WEIGHT_USER real                               '
    ')                                              '
    )

cursor.execute(
    'insert into users (NAME_USER, WEIGHT_USER) '
    'values (?,?)                               ',
    ('Ana', 50.4)
)

cursor.execute(
    'insert into users (NAME_USER, WEIGHT_USER) '
    'values (:name,:weight)                               ',
    {'name': 'João', 'weight': 60.6}
)

cursor.execute(
    'insert into users '
    'values (:id, :name, :weight)                               ',
    {'id': None, 'name': 'Daniel', 'weight': 82.6}
)

conexao.commit()


cursor.execute(
    'update users set NAME_USER = :name, WEIGHT_USER = :weight where ID_USER = :id',
    {'name': 'Pedro','weight': '78.1', 'id': 2}
)


cursor.execute(
    'delete from users where ID_USER = :id',
    {'id': 5}
)
"""

cursor.execute(
    'select NAME_USER, WEIGHT_USER from users where WEIGHT_USER > :weight',
    {'weight': 55}
)

for line in cursor.fetchall():
    name, weight = line
    print(name, weight)

cursor.close()
conexao.close()