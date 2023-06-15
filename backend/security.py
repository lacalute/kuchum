from config import *

@app.post('/login', tags=['security'])
def login(login: Login, req: Request, Authorize: AuthJWT = Depends()):
  if token.get_access_token(req) == None and token.get_refresh_token(req) == None:
    user_payload = usrs.find_one({'nick': login.nick})
    if check_hashing(login.password, user_payload['password']):
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
    if usrs.find_one({'email': user.email}) == None and usrs.find_one({'nick': user.nick}) == None:
      user_payload = crud_user.create_user(user.fname, user.lname, user.nick, user.email, hashing(user.password))
      Authorize.set_access_cookies(token.create_access_token(str(user_payload['_id'])))
      Authorize.set_refresh_cookies(token.create_refresh_token())
      return {"msg":"Successfully login"}
    else:
      return {'msg': 'Creditionals is using righ now'}
  return {'msg': 'You are logged in now'}

