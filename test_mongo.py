from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Check available databases
db_list = client.list_database_names()

print("✅ MongoDB Connection Successful!")
print("📂 Available Databases:", db_list)
