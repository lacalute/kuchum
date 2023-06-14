from config import *

token = Token()

@app.post('/login', tags=['security'])
def login(login: Login, req: Request, Authorize: AuthJWT = Depends()):
  if token.get_access_token(req) == None and token.get_refresh_token(req) == None:
    user_payload = usrs.find_one({'nick': login.nick, 'password': login.password})
    if user_payload:
      Authorize.set_access_cookies(token.create_access_token(str(user_payload['_id'])))
      Authorize.set_refresh_cookies(token.create_refresh_token())
      return {"msg":"Successfully login"}
    return {'User not found'}
  return {'msg': 'You are logged in now'}

@app.delete('/logout', tags=['security'])
async def logout (Authorize: AuthJWT = Depends()):
  Authorize.unset_jwt_cookies()
  return {"STATUS": "OK"}

@app.get('/protected', tags=['security'])
def protected(request: Request, Authorize: AuthJWT = Depends()):
  if token.isAccessToken(request, Authorize) and token.isRefreshToken(request, Authorize):
    return token.decodeToken(token.get_access_token(request))
  return {'Access is closed'}

@app.post('/registration', tags=['security'])
def register(req:Request, user: Registration, Authorize: AuthJWT = Depends()):
  if token.get_access_token(req) == None and token.get_refresh_token(req) == None:
    crud_user = CrudUser(user.fname, user.lname, user.nick, user.email, user.password)
    user_payload = crud_user.create()
    Authorize.set_access_cookies(token.create_access_token(user_payload['_id']))
    Authorize.set_refresh_cookies(token.create_refresh_token())
    return {"msg":"Successfully login"}
  return {'msg': 'You are logged in now'}

