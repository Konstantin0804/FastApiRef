import os

import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import motor.motor_asyncio

load_dotenv()

DATABASE_NAME = "todo-db"
CONTAINER_NAME = "todo-items"


user = os.getenv("MONGO_NAME")
password = os.getenv("MONGO_PASS")
db_address = os.getenv("MONGO_IP")

MONGO_URI = (f'mongodb+srv://{user}:{password}@{db_address}/?w=majority&appName=Cluster0')
print(MONGO_URI)

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI, tlsCAFile=certifi.where())
db = mongo_client.practice_db
