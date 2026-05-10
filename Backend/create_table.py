import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    region TEXT NOT NULL,
    sales REAL NOT NULL
)
''')

# Commit and close
conn.commit()
conn.close()

print("Table created successfully!")
