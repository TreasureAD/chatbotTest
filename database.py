import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('user_interactions.db')
cursor = conn.cursor()

# Create the User Interactions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS UserInteractions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        question TEXT,
        timestamp TEXT
    )
''')
conn.commit()

def store_user_interaction(user_id, question):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO UserInteractions (user_id, question, timestamp) VALUES (?, ?, ?)', (user_id, question, timestamp))
    conn.commit()

def get_all_user_interactions():
    cursor.execute('SELECT * FROM UserInteractions')
    return cursor.fetchall()

# Add other database operations as needed
