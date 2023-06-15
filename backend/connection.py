# the connection was copied from mongo docs
from pymongo import MongoClient
uri = "mongodb+srv://sample:Poher_123@cluster0.zcsjtwf.mongodb.net/"
client = MongoClient(uri)
db = client['sample_mflix']
usrs = db['usrs']
posts = db['psts']


