import sqlite3

# Connect to SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('starcraft.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define a SQL query to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);
'''

create_table_query2 = '''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
);
'''

create_table_gate = '''
CREATE TABLE IF NOT EXISTS game
'''


# Execute the query to create the table
cursor.execute(create_table_query2)

# Commit the changes and close the connection
conn.commit()
conn.close()