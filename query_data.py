import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Query to get all data from the sales table
cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Print all rows in the sales table
for row in rows:
    print(row)

conn.close()
