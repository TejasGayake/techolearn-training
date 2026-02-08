import pandas as pd
import sqlite3

# data is need to be connect using Connection() funciton
# if not exist then this function create it
conn = sqlite3.Connection("First_database.db")

# need to create cursor for execute SQL queries
# inbuilt function in python 
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER,
               email TEXT UNIQUE)
""")


# commit() = Save Changes  
# Calling conn.commit() tells SQLite: “Write everything from memory into the actual database file.” Without it, your changes may be lost if the program ends.
conn.commit()