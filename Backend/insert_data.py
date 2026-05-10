import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Insert some sample data into the sales table
sales_data = [
    ('2024-01-01', 'Laptop', 'North America', 1500.0),
    ('2024-01-05', 'Phone', 'Europe', 800.0),
    ('2024-02-01', 'Tablet', 'Asia', 600.0),
]

cursor.executemany('''
INSERT INTO sales (date, product, region, sales)
VALUES (?, ?, ?, ?)
''', sales_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Sample data inserted successfully!")
