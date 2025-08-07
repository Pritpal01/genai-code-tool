from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.codemate
submissions = db.submissions

def save_submission(code, summary, debug_output):
    entry = {
        "code": code,
        "summary": summary,
        "debug_output": debug_output,
        "timestamp": datetime.utcnow()
    }
    submissions.insert_one(entry)
