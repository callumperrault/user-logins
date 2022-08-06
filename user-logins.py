import hashlib
import sqlite3
from urllib.request import HTTPBasicAuthHandler

db_name = 'ppab6.db'

def is_valid_credentials(username, password):
    # Connection is made to database and cursor is created
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Password is hashed here
    hashed_password = hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()
    
    # Username and password are compared to the ones in the config file, True is returned if they
    # match and false is returned otherwise
    cursor.execute('''SELECT rowid FROM users WHERE usernames = ?''', (username,))
    username_ = cursor.fetchone()

    cursor.execute('''SELECT rowid FROM users WHERE hashed_passwords = ?''', (hashed_password,))
    password_ = cursor.fetchone()
    return((username_ is not None) and  (password_ is not None))

while True:
    
    username = input("What is your username?\n")
    password = input("What is your password?\n")

    if is_valid_credentials(username, password):
        print("Username and password are correct. Granting access now")
        break

    else:
        print("Username or password is incorrect. Please try again")
            


        