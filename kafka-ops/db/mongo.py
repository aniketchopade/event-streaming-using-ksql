import pymongo
import os
    
def get_database():
    from pymongo import MongoClient


    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.environ["CONNECTION_STRING"]

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['bank']

def query(dbname, collection_name):    
    # Create a new collection
    collection_name = dbname[collection_name]
    item_details = collection_name.find()
    return item_details;
    
    # This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    # Get the database
    dbname = get_database()
    query(dbname)