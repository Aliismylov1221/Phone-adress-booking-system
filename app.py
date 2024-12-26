from flask import Flask, jsonify, request
from controller import ContactController
from models import Contact

app = Flask(__name__)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    """Fetch all contacts."""
    contacts = ContactController.get_all_contacts()
    return jsonify([contact.to_dict() for contact in contacts])

@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    """Fetch a specific contact by ID."""
    contact = ContactController.get_contact_by_id(id)
    if contact:
        return jsonify(contact.to_dict())
    return jsonify({"message": "Contact not found"}), 404

@app.route('/contacts', methods=['POST'])
def create_contact():
    """Create a new contact."""
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    if name and phone and email:
        ContactController.add_contact(name, phone, email)
        return jsonify({"message": "Contact added successfully"}), 201
    return jsonify({"message": "Invalid data"}), 400

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    """Update an existing contact."""
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    contact = ContactController.get_contact_by_id(id)
    if contact:
        ContactController.update_contact(id, name, phone, email)
        return jsonify({"message": "Contact updated successfully"})
    return jsonify({"message": "Contact not found"}), 404

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    """Delete a contact."""
    contact = ContactController.get_contact_by_id(id)
    if contact:
        ContactController.delete_contact(id)
        return jsonify({"message": "Contact deleted successfully"})
    return jsonify({"message": "Contact not found"}), 404

if __name__ == '__main__':
    from database import init_db
    init_db()  # Initialize the database
    app.run(debug=True)
