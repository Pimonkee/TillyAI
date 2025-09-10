from pymongo import MongoClient
from bson.objectid import ObjectId
from src.config import get_config


# Initialize MongoDB client and database
config = get_config('development')
mongo_client = MongoClient(config.MONGO_URI)
db = mongo_client.get_database()


class User:
    collection = db.users

    @staticmethod
    def create_user(user_data):
        """Create a new user in the MongoDB database."""
        result = User.collection.insert_one(user_data)
        return result.inserted_id

    @staticmethod
    def get_user(user_id):
        """Retrieve a user by their ID."""
        if isinstance(user_id, str):
            user_id = ObjectId(user_id)
        return User.collection.find_one({"_id": user_id})

    @staticmethod
    def update_user(user_id, update_data):
        """Update user details."""
        if isinstance(user_id, str):
            user_id = ObjectId(user_id)
        result = User.collection.update_one({"_id": user_id}, {"$set": update_data})
        return result.modified_count

    @staticmethod
    def delete_user(user_id):
        """Delete a user from the database."""
        if isinstance(user_id, str):
            user_id = ObjectId(user_id)
        result = User.collection.delete_one({"_id": user_id})
        return result.deleted_count