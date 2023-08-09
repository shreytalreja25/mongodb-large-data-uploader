import json
from pymongo import MongoClient
import sys

# Specify the JSON file path
json_file_path = r'C:\\Users\\Piyush Ratta\\Desktop\\formy.json'

# MongoDB connection settings
mongo_uri = "mongodb://localhost:27017/"  # Update with your MongoDB URI
db_name = "RCM"
collection_name = "billdata"

# Define the chunk size
chunk_size = 1000
total_rows_to_upload = 1000000

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

# Define the progress bar function
def print_progress_bar(iteration, total, prefix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
    sys.stdout.flush()

# Insert data into the collection with progress bar
total_documents = len(data)
chunks_to_upload = min(total_rows_to_upload, total_documents) // chunk_size

for chunk_index in range(chunks_to_upload):
    start_index = chunk_index * chunk_size
    end_index = start_index + chunk_size
    chunk_data = data[start_index:end_index]

    collection.insert_many(chunk_data)

    print_progress_bar(chunk_index + 1, chunks_to_upload, prefix='Progress:', length=50)

print("\nData inserted successfully.")
