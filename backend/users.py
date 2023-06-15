from config import *

crud_users = CRUD(usrs)

@app.post('/delete_user', tags=['users'])
async def delete_user(id):
  return crud_users.delete(id)

@app.get('/users', tags=['users'])
async def all_users():
  return crud_users.get_all()
    

@app.get('/user/{id}', tags=['users'])
async def user_id(id):
  try:
    return crud_users.get_id(id)
  except:
    return "User not found"
  
