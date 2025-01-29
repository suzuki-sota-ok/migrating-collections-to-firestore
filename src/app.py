import firebase_admin
from firebase_admin import credentials, firestore
import json
import logging

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('secret/secret.json')
firebase_admin.initialize_app(cred)

# Get user inputs
input_database_id = input('Enter the database ID: ')
input_file_name = input('Enter the file name without extension (make sure the file name matches the collection name): ')

# Initialize Firestore client
db = firestore.client(database_id=input_database_id)
data_path = f"data/{input_file_name}.json"
logger.info(f"Data path: {data_path}")

# Load JSON data
with open(data_path, 'r') as file:
    data = [json.loads(line) for line in file]

# Transform data
transformed_data = {
    item['_id']['$oid']: {k: v for k, v in item.items() if k not in ['__v', '_id']}
    for item in data
}


def chunk_data(data, chunk_size):
    """Yield successive chunks from data."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def batch_write(data, collection_name, chunk_size=500):
    """Write data to Firestore in batches."""
    for chunk in chunk_data(list(data.items()), chunk_size):
        batch = db.batch()
        for document_id, document_data in chunk:
            try:
                doc_ref = db.collection(collection_name).document(document_id)
                batch.set(doc_ref, document_data)
            except Exception as e:
                logger.error(f'Error setting document {document_id}: {e}')
        try:
            batch.commit()
        except Exception as e:
            logger.error(f'Error committing batch: {e}')
    logger.info('Data uploaded successfully')


# Upload data to Firestore
batch_write(transformed_data, input_file_name)