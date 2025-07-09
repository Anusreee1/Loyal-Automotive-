import sqlite3

# Connect to your database file
conn = sqlite3.connect('loyal_automotive.db')  # Make sure file exists in your folder

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# (Optional) Check connection
print("Connected to database successfully!")

conn.close()
