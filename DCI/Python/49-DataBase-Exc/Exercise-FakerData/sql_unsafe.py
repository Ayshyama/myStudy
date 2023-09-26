import sqlite3

conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# username = input("enter new username: ")
# username = 'Robert"); DROP TABLE user; --'
# insert_query = f'INSERT INTO user (username) VALUES ("{username}");'
# cursor.executescript(insert_query)


select_query = 'SELECT username FROM user WHERE id = (SELECT MAX(id) FROM user);'
cursor.executescript(select_query)

rows = cursor.fetchall()
for row in rows:
    print(row)


conn.commit()
conn.close()

# print("a new username has been inserted")

