from config import *
from schemes import Login, Registration
from tokens import *
from payloads import *

crud_security = CRUD(usrs)


@app.post('/login', tags=['security'])
def login(login: Login, req: Request, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, 1, Authorize)
  user_payload = usrs.find_one({'nick': login.nick})

  if check_hashing(login.password, user_payload['password']):
    Authorize.set_access_cookies(token.create_access_token(str(user_payload['_id'])))
    Authorize.set_refresh_cookies(token.create_refresh_token())
    return {"msg":"Successfully login"}
  return {'msg': 'Creditionals are bad'}

@app.delete('/logout', tags=['security'])
async def logout (Authorize: AuthJWT = Depends()):
  Authorize.unset_jwt_cookies()
  return {"msg": "OK"}

@app.get('/profile', tags=['security'])
def profile(req: Request, Authorize: AuthJWT = Depends()):
  tokens = token.tokens_required(req, 2, Authorize)
  return crud_security.get_id(tokens['access']['user_id'])


@app.post('/registration', tags=['security'])
def register(req:Request, user: Registration, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, 1, Authorize)
  if usrs.find_one({'email': user.email}) == None:
    if usrs.find_one({'nick': user.nick}) == None:
      payload = user_payload(user.fname, user.lname, user.nick, user.email, user.password)
      crud_security.create(payload)
      Authorize.set_access_cookies(token.create_access_token(str(payload['_id'])))
      Authorize.set_refresh_cookies(token.create_refresh_token())
      return {"msg":"Successfully login"}
    else:
      return {'msg': 'Nick are using now'}
  else:
    return {'msg': 'Email are using now'}
  

