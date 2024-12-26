import sqlite3
from sqlite3 import Error

def create_connection():
    """Create and return a database connection."""
    conn = None
    try:
        conn = sqlite3.connect('address_book.db')
    except Error as e:
        print(e)
    return conn

def init_db():
    """Initialize the database with a Contacts table."""
    conn = create_connection()
    if conn:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        );
        """
        conn.execute(create_table_query)
        conn.commit()
        conn.close()
