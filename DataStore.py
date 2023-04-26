# please note, the database file will have to be populated below with 
# the required database information and currently stands as a placeholder within the code

import sqlite3

# create a database
conn = sqlite3.connect('information_security.db')
c = conn.cursor()

# create tables
c.execute('''CREATE TABLE IF NOT EXISTS information_assets
             (id INTEGER PRIMARY KEY, name TEXT, type TEXT, classification TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS policies
             (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS procedures
             (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS roles
             (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

# insert data
c.execute("INSERT INTO information_assets (name, type, classification) VALUES (?, ?, ?)", ('Server', 'Hardware', 'Confidential'))
c.execute("INSERT INTO policies (name, description) VALUES (?, ?)", ('Password Policy', 'Defines rules for creating and managing passwords'))
c.execute("INSERT INTO procedures (name, description) VALUES (?, ?)", ('Incident Response Procedure', 'Defines the steps to be taken in the event of a security incident'))
c.execute("INSERT INTO roles (name, description) VALUES (?, ?)", ('Information Security Officer', 'Responsible for overseeing the organization\'s information security program'))

# commit changes and close connection
conn.commit()
conn.close()
