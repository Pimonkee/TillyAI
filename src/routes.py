
### **`src/routes.py`**

```python
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
```

### Description:
- **Blueprint Creation**: Creates a `Blueprint` named `user`, which is used to organize and modularize routes related to user operations.
- **Routes**:
  - **`/user` (POST)**: Creates a new user. Validates and sanitizes input, then uses the `User` model to insert a new document into MongoDB.
  - **`/user/<user_id>` (GET)**: Retrieves a user by their ID using the `User` model and returns the user details.
  - **`/user/<user_id>` (PUT)**: Updates user details. Validates and sanitizes input, then updates the user document in MongoDB.
  - **`/user/<user_id>` (DELETE)**: Deletes a user by their ID using the `User` model.

### Usage:
1. **Register Blueprint**:
   In your `create_app` function or similar setup code, register the `user_blueprint`:
   ```python
   from src.routes import user_blueprint

   app = create_app('development')
   app.register_blueprint(user_blueprint)
   ```

2. **Testing Routes**:
   Use tools like `curl`, Postman, or your web browser to test the various endpoints:
   - **Create User**: Send a POST request to `/user` with a JSON body containing `name` and `email`.
   - **Get User**: Send a GET request to `/user/<user_id>`.
   - **Update User**: Send a PUT request to `/user/<user_id>` with a JSON body containing fields to update.
   - **Delete User**: Send a DELETE request to `/user/<user_id>`.

### Benefits:
- **Organizational Clarity**: Separates route definitions from application setup and logic, making it easier to manage and extend.
- **Modular Design**: Allows you to define routes in a modular way using blueprints, promoting cleaner and more maintainable code.
- **Reusability**: Makes it easier to reuse and test route handlers separately from the rest of the application.

Including a `routes.py` file helps structure your Flask application by organizing route handlers in a modular fashion, improving the maintainability and scalability of your codebase.