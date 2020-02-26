from pymongo import MongoClient
from eqobject.config import settings

db = MongoClient(settings.MONGODB_URI)[settings.MONGODB_DATABASE]


def reset_database():
    db.drop()
    db.find()
    
