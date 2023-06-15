from config import *
from schemes import Login, Registration
from tokens import *

crud_security = CRUD(usrs)


@app.post('/login', tags=['security'])
def login(login: Login, req: Request, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, 1, Authorize)
  user_payload = usrs.find_one({'nick': login.nick})
  if check_hashing(login.password, user_payload['password']):
    Authorize.set_access_cookies(token.create_access_token(str(user_payload['_id'])))
    Authorize.set_refresh_cookies(token.create_refresh_token())
    return {"msg":"Successfully login"}
  return {'msg': 'You are logged in now'}

@app.delete('/logout', tags=['security'])
async def logout (Authorize: AuthJWT = Depends()):
  Authorize.unset_jwt_cookies()
  return {"msg": "OK"}

@app.get('/protected', tags=['security'])
def protected(request: Request, Authorize: AuthJWT = Depends()):
  token.tokens_required(request, 2, Authorize)
  return {'Access is good'}

@app.post('/registration', tags=['security'])
def register(req:Request, user: Registration, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, option=1)
  if usrs.find_one({'email': user.email}) == None:
    if usrs.find_one({'nick': user.nick}) == None:
      user_payload = crud_security.create_user(user.fname, user.lname, user.nick, user.email, hashing(user.password))
      Authorize.set_access_cookies(token.create_access_token(str(user_payload['_id'])))
      Authorize.set_refresh_cookies(token.create_refresh_token())
      return {"msg":"Successfully login"}
    else:
      return {'msg': 'Nick are using now'}
  else:
    return {'msg': 'Email are using now'}
  

