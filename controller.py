from models import Contact
import sqlite3
from database import create_connection

class ContactController:
    @staticmethod
    def get_all_contacts():
        """Get all contacts from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        contacts = [Contact(id=row[0], name=row[1], phone=row[2], email=row[3]) for row in rows]
        conn.close()
        return contacts

    @staticmethod
    def get_contact_by_id(contact_id):
        """Get a contact by ID."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Contact(id=row[0], name=row[1], phone=row[2], email=row[3])
        return None

    @staticmethod
    def add_contact(name, phone, email):
        """Add a new contact to the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        conn.close()

    @staticmethod
    def update_contact(contact_id, name, phone, email):
        """Update an existing contact in the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_contact(contact_id):
        """Delete a contact from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        conn.close()
