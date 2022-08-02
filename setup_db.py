import sqlite3
import os

db_name = "ppab6.db"

if __name__ == "main":
    # If database already exists, it checks if user wants to create a new one before overwriting
    # the old one
    if os.path.isfile(db_name):
        while True:
            user_input = input("Database " + db_name + "already exists. Should I overwrite it? [y/n]")

            if user_input == "y":
                print("Ok deleting the database and creating a new one.")
                os.remove(db_name)
                break
            elif user_input == "n":
                print("Ok. Database will not be overwritten.")
                exit(0)
            else:
                print("Please enter 'y' or 'n'")

# Provides connection to database for the cursor to use                
connection = sqlite3.connect('ppab6.db')

# Cursor created to invoke SQLite methods
cursor = connection.cursor()

# creates new table that will store the usernames and passwords
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users
    ([usernames] CHARVAR, [hashed_passwords] CHARVAR)
''')

connection.commit()

print("Your database has been created.")
