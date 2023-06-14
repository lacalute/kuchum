from config import *


@app.post('/all_users', tags=['users'])
def all_users():
  all_users = []
  for user in usrs.find():
    user['_id'] = str(user['_id'])
    all_users.append(user)
  return all_users
