from pymongo import MongoClient

def get_db_client(uri="mongodb://localhost:27017/", db_name="chatbot_db"):
    client = MongoClient(uri)
    return client[db_name]

def log_conversation(db, user_query, bot_response):
    conversation = {
        "query": user_query,
        "response": bot_response
    }
    db.conversations.insert_one(conversation)
