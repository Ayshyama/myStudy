import psycopg2

conn = psycopg2.connect(database='test',
                        host='localhost',
                        user='postgres',
                        password='153957')

cur = conn.cursor()

cur.execute('''drop table if exists users;''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    );
''')

val = [(2, 'Alex', 17), (4, 'Alex', 17), (6, 'Alex', 17),]
cur.executemany('''insert into users values (%s, %s, %s);''', val)

cur.execute('''select * from users;''')

print(*cur.fetchall(), sep='\n')

print(cur.statusmessage)
print(cur.rowcount)
print(cur.query)
print(cur.description)
print(cur.connection)
print(cur.lastrowid)
print(cur.arraysize)
print(cur.__dir__)

conn.commit()
cur.close()
conn.close()



# cur.execute('''select datname from pg_database;''')

# cur.execute('''select tablename from pg_tables ;''')