from flask import Blueprint, request, jsonify
from src.models import User
from src.utils import validate_email, sanitize_input


# Create a Blueprint for user-related routes
user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    name = sanitize_input(data['name'])
    email = sanitize_input(data['email'])
    
    if not validate_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    user_id = User.create_user({"name": name, "email": email})
    return jsonify({"user_id": str(user_id)}), 201


@user_blueprint.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by their ID."""
    user = User.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Convert ObjectId to string for JSON serialization
    user['_id'] = str(user['_id'])
    return jsonify(user), 200


@user_blueprint.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user details."""
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    update_data = {}
    if 'name' in data:
        update_data['name'] = sanitize_input(data['name'])
    if 'email' in data:
        email = sanitize_input(data['email'])
        if not validate_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        update_data['email'] = email
    
    if not update_data:
        return jsonify({"error": "No fields to update"}), 400

    modified_count = User.update_user(user_id, update_data)
    if modified_count == 0:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({"message": "User updated"}), 200


@user_blueprint.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user from the database."""
    deleted_count = User.delete_user(user_id)
    if deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({"message": "User deleted"}), 200


# Add Tilly AI processing route
@user_blueprint.route('/tilly', methods=['POST'])
def tilly_response():
    """Process input through Tilly AI."""
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, 'text' field required"}), 400
    
    user_input = sanitize_input(data['text'])
    # For now, return a simple response - this can be expanded with actual AI processing
    response = f"Received and processed: {user_input}"
    
    return jsonify({"response": response}), 200