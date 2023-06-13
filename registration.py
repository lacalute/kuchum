from config import *

@app.post('/registration')
def register(user: User, Authorize: AuthJWT = Depends()):
  user_payload = collection.create(user.fname, user.lname, user.nick, user.email, user.password)
  access_token = jwt.encode({'id': user_payload}, 'secret', 'HS256')
  refresh_token = jwt.encode({'id': user_payload}, 'secret', 'HS256')
  Authorize.set_access_cookies(access_token)
  Authorize.set_refresh_cookies(refresh_token)
  return {"msg":"Successfully login"}


