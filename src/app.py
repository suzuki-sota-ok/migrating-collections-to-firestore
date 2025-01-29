import firebase_admin
from firebase_admin import credentials, firestore
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('secret/secret.json')
firebase_admin.initialize_app(cred)

input_database_id = input('Enter the database ID: ')
input_file_name = input('Enter the file name without extension (make sure the file name matches the collection name): ')

db = firestore.client(database_id=input_database_id)
data_path = "data/{}.json".format(input_file_name)

# Load JSON data
with open(data_path, 'r') as file:
    data = json.load(file)

# Upload data to Firestore
# Set data in each document within the 'data' collection
try:
    for document_id, document_data in data.items():
        doc_ref = db.collection(input_file_name).document(document_id)
        doc_ref.set(document_data)
except Exception as e:
    logger.error('Error uploading data: {}'.format(e))

logger.info('Data uploaded successfully')