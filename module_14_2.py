import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     username = f"User{i}"
#     email = f"example{i}@gmail.com"
#     age = i * 10
#     balance = 1000
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (username, email, age, balance))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = 500 WHERE id = ?", (i,))
#
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# rows = cursor.fetchall()
#
# for row in rows:
#     print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")


cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
