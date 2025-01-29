# Migrating Collections to Firestore

This project demonstrates how to migrate collections to Firestore using Python.

## Prerequisites

- Python 3.12 or higher
- Google Cloud SDK
- Firestore client library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/migrating-collections-to-firestore.git
    cd migrating-collections-to-firestore
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r src/requirements.txt
    ```

## Configuration

1. Create a Firebase project and generate a private key file for the service account.
2. Save the generated private key file as `secret.json` and place it in the `secret` folder.
3. Place the data you want to set in Firestore in the `data` folder.
    - Ensure that the file name matches the database collection name.

## Usage

Run the migration script:
```sh
python src/app.py
```
