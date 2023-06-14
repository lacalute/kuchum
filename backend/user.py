from config import *

@app.get('/users', tags=['users'])
async def all_users():
  all_users = []
  for user in usrs.find():
    user['_id'] = str(user['_id'])
    all_users.append(user)
  return all_users

@app.get('/user/{id}', tags=['users'])
async def user_id(id):
  try:
    user_id = usrs.find_one({'_id': ObjectId(id)})
    user_id['_id'] = str(user_id['_id'])
    return user_id
  except:
    return "Post not found"