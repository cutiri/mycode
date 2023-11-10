import sqlite3

DBNAME = 'starcraft.db'

class DB:
    def __init__(self) -> None:
        #self.conn = sqlite3.connect(DBNAME)
        pass

    def connect(self):
        return sqlite3.connect('starcraft.db')
    
    def getCursor(self):
        return self.connect().cursor()

    def login(self, username, password):
        query = "SELECT username FROM users WHERE username = '{0}' AND password = '{1}'".format(username, password)
        #print(self.connectThenRun(query))
        return self.connectThenRun(query)

    def connectThenRun(self, query):
        conn = sqlite3.connect(DBNAME)
        cursor = conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        #print(query)
        #print("records: ", records)
        conn.commit()
        conn.close()
        #print("records: ", records)
        return records

    def dbInitialize(self):
        # Connect to SQLite database (this will create a new database if it doesn't exist)
        conn = sqlite3.connect(DBNAME)

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

        cursor.execute("INSERT INTO users (username,password) VALUES ('{0}','{1}')".format('user1', 'pass'))
        cursor.execute("INSERT INTO users (username,password) VALUES ('{0}','{1}')".format('user2', 'pass'))
        cursor.execute("INSERT INTO users (username,password) VALUES ('{0}','{1}')".format('user3', 'pass'))


        # Execute the query to create the table
        cursor.execute(create_table_query2)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()




if __name__ == "__main__":
    database = DB()
    database.dbInitialize()