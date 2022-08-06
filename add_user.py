import hashlib
import sqlite3

db_name = "ppab6.db"

def username_not_taken(username_):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''SELECT rowid FROM users WHERE usernames = ?''', (username_,))
    data = cursor.fetchone()

    return(data is None)

def insert_user(username, password):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    hashed_password = hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()

    cursor.execute('''INSERT INTO users(usernames, hashed_passwords) VALUES (?, ?)''', (username, hashed_password))
    connection.commit()

print("Time to create your account!\n")

while True:
    username = input("Please enter your username: \n")

    if username_not_taken(username):
        break
    else:
        print("Username is taken, please enter a new username: \n")

password = input("Please enter your password: \n")

insert_user(username, password)

print("Successfully registered")