import sqlite3

from faker import Faker

fake = Faker()

sqlquery = '''
DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50),
    email VARCHAR(50),
    birthdate DATE,
    country VARCHAR(50)
);
INSERT INTO user (username, email, birthdate, country) VALUES
'''
values = []

for i in range(5):
    values.append(f'("{fake.name()}", "{fake.email()}", "{fake.date()}", "{fake.country()}")')

sqlquery += ',\n'.join(values) + ';'
print(sqlquery)


with open('data.sql', 'w', encoding='UTF-8') as file:
    file.write(sqlquery)

conn = sqlite3.connect('user_database.db')
cur = conn.cursor()

with open('data.sql') as dtsql:
    cur.executescript(dtsql.read())

print(*cur.execute('SELECT * FROM user').fetchall(), sep='\n')
conn.close()