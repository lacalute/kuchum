from config import *

crud_users = CRUD(usrs)

@app.post('/delete_user', tags=['users'])
async def delete_user(id):
  return crud_users.delete(id)

@app.get('/users', tags=['users'])
async def all_users():
  return crud_users.get_all()
    

@app.get('/user/@{nick}', tags=['users'])
async def user_nick(nick):
  try:
    result = usrs.find_one({'nick': nick})
    result["_id"] = str(result["_id"])
    return result
  except:
    return "User not found"
  
