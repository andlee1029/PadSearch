import json
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

db = myclient['padsearch-db']

with open('raw/raw-jsons/monsters.json') as f:
    file_data = json.load(f)

Collection = db['monstersearch_monster']
Collection.delete_many({})
if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)


with open('raw/raw-jsons/skills.json') as f:
    skill_file_data = json.load(f)
Collection = db['monstersearch_skill']
Collection.delete_many({})
if isinstance(file_data, list):
    Collection.insert_many(skill_file_data)
else:
    Collection.insert_one(file_data)

