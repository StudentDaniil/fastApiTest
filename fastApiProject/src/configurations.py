from envparse import Env
from pymongo.mongo_client import MongoClient

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/mongo_db")

client = MongoClient(MONGODB_URL)

db = client.message

collection = db["message"]

