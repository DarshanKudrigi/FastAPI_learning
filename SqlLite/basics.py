# SQLite

# is a database.

# SQLAlchemy

# is a Python SQL toolkit / ORM that helps your Python application work with relational databases.


# Write a Python program that connects to a SQLite database, creates a table, inserts some data, and retrieves the data.
import sqlite3
import os
import sys
import logging
import pandas as pd
import numpy as np
import fastapi as FastAPI


app = FastAPI()
# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert some data
cursor.execute("INSERT INTO employees (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO employees (name, age) VALUES ('Bob', 25)")

# Commit the changes
conn.commit()

# Retrieve the data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()

