from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]

def save_pregnancy_data(user_id, lmp, due_date):
    """Save pregnancy tracking data to the database."""
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"lmp": lmp, "due_date": due_date}},
        upsert=True
    )

def get_pregnancy_data(user_id):
    """Retrieve user's pregnancy tracking data."""
    return users_collection.find_one({"user_id": user_id})
