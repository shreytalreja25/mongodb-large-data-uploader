import json
from pymongo import MongoClient
import sys

# Specify the JSON file path
json_file_path = r'C:\\Users\\Piyush Ratta\\Desktop\\formy.json'

# MongoDB connection settings
mongo_host = 'localhost'  # Change this to your MongoDB host
mongo_port = 27017       # Change this to your MongoDB port
db_name = 'RCM'
collection_name = 'billdata'

# Function to upload a chunk of data to MongoDB
def upload_chunk(chunk):
    client = MongoClient(mongo_host, mongo_port)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(chunk)
    client.close()

# Read the JSON file and upload in chunks
chunk_size = 1000
data = []

with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    data_records = json_data["main"]["DATA_RECORD"]
    
    for record in data_records:
        data.append(record)
        if len(data) == chunk_size:
            upload_chunk(data)
            data = []

# Upload the remaining data (less than a full chunk)
if data:
    upload_chunk(data)
    data = []

print("Data upload complete.")
