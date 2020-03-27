from pymongo import MongoClient

conn = MongoClient('localhost', 27027)
db = conn.cadastrodb

collection = db.cadastrodb

import datetime

post1 = {"codigo": "ID-9987725",
"prod_name": "Geladeira",
"marcas": ["brastemp", "consul", "electrolux"],
"data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id
post_id