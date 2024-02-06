import os
import json
from pymongo import MongoClient
from datetime import datetime


class JsonToMongo:
    def __init__(self, db_url='mongodb://localhost:27017', db_name='PDB_StudentVers', collection_name='students'):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_collection(self):
        if self.collection.name not in self.db.list_collection_names():
            print(f"Collection '{self.collection.name}' does not exist. Creating...")
            self.db.create_collection(self.collection.name)
            print(f"Collection '{self.collection.name}' created.")

    def insert_data(self, repo_path):
        for filename in os.listdir(repo_path):
            if filename.endswith("_etudiant.json"):
                filepath = os.path.join(repo_path, filename)
                with open(filepath, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)

                print(f"Inserting data from {filename} into '{self.collection.name}' collection...")
                self.collection.insert_many(data)
                print(f"Data from {filename} inserted successfully.")

                # Update metadata
                self.update_metadata(data)

    def update_metadata(self, data):
        for student in data:
            filter_query = {"matricule": student["matricule"]}
            update_query = {
                "$set": {
                    "metadata.updated.At.$date.$numberLong": str(datetime.utcnow().timestamp() * 1000)
                }
            }
            self.collection.update_one(filter_query, update_query)

            # Update created metadata only if $numberLong is 0
            if student["metadata"]["created"]["At"]["$date"]["$numberLong"] == "0":
                update_created_query = {
                    "$set": {
                        "metadata.created.At.$date.$numberLong": str(datetime.utcnow().timestamp() * 1000)
                    }
                }
                self.collection.update_one(filter_query, update_created_query)

            print(f"Metadata updated for student with matricule {student['matricule']}.")

    def close_connection(self):
        self.client.close()


# Example usage
if __name__ == "__main__":
    json_to_mongo = JsonToMongo()
    json_to_mongo.create_collection()

    folder_path = "/mnt/9EDE2F40DE2F0FD7/Stage/X3/Bonus/utilities"
    json_to_mongo.insert_data(folder_path)

    json_to_mongo.close_connection()
