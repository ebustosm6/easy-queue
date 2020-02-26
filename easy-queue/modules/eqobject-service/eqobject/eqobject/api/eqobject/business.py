from eqobject.database import db
from easyqueue.core.base import EQObject


def create_eq_object(eq_obj):
    if (isinstance(eq_obj, dict)):
        eq_object = EQObject.from_json(eq_obj)
    else:
        eq_object = eq_obj
    
    mongo_result = db.eqobject.insert_one(eq_object.json())
    return dict(acknowledged=mongo_result.acknowledged, inserted_id=mongo_result.inserted_id)

def create_eq_objects(eq_objs):
    eq_objects = []
    
    for eq_obj in eq_objs:
        if (isinstance(eq_obj, EQObject)):
            eq_objects.append(eq_obj.json())
        else:
            eq_objects.append(eq_obj)
    
    mongo_result = db.eqobject.insert_many(eq_objects)
    return dict(acknowledged=mongo_result.acknowledged, inserted_ids=mongo_result.inserted_ids)

def request_eq_object(eqobject_id):
    if not isinstance(eqobject_id, str):
        raise ValueError("eqobject_id must be string")
    
    eqobject_json = db.eqobject.find_one({"_id": eqobject_id})
    return EQObject.from_json(eqobject_json)

def update_eq_object(eqobject_id, eq_obj):
    if not isinstance(eqobject_id, str):
        raise ValueError("eqobject_id must be string")

    if (isinstance(eq_obj, dict)):
        eq_object = EQObject.from_json(eq_obj)
    else:
        eq_object = eq_obj
        
    mongo_result = db.eqobject.update_one({ '_id': eqobject_id}, {"$set":eq_object.json()})
    return dict(acknowledged=mongo_result.acknowledged, modified_count=mongo_result.modified_count)

def delete_eq_object(eqobject_id):
    if not isinstance(eqobject_id, str):
        raise ValueError("eqobject_id must be string")
    
    mongo_result = db.eqobject.delete_one({ '_id': eqobject_id})
    return dict(acknowledged=mongo_result.acknowledged)

def request_eq_objects(skip=None, limit=None):
    if skip and limit:
        if not (isinstance(skip, int) and isinstance(limit, int) or skip < 0 or limit < 0):
            raise ValueError("params must be positive integers")
        mongo_result = db.eqobject.find().skip(skip).limit(limit)

    elif skip and not limit:
        if not isinstance(skip, int) or skip < 0:
            raise ValueError("skip param must be positive integer")
        mongo_result = db.eqobject.find().skip(skip)
    
    elif limit and not skip:
        if not isinstance(limit, int) or limit < 0:
            raise ValueError("limit must be positive integer")
        mongo_result = db.eqobject.find().limit(limit)

    else:
        mongo_result = db.eqobject.find()

    eq_object = [EQObject.from_json(eq_json) for eq_json in mongo_result]

    return eq_object