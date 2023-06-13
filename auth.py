from config import *


@app.post('/login')
def login(login: Login, Authorize: AuthJWT = Depends()):
    user_response = usrs.find_one({'nick': login.nick, 'password': login.password})
    if user_response:

      # Create the tokens and passing to set_access_cookies or set_refresh_cookies
      access_token = jwt.encode({'id': str(user_response['_id'])}, 'secret', 'HS256')
      refresh_token = jwt.encode({'id': str(user_response['_id'])}, 'secret', 'HS256')

      # Set the JWT cookies in the response
      Authorize.set_access_cookies(access_token)
      Authorize.set_refresh_cookies(refresh_token)
      return {"msg":"Successfully login"}
    return {'User not found'}
@app.post('/refresh')
def refresh(request: Request, Authorize: AuthJWT = Depends()):
    if check_tokens(request):   
      token = request.cookies.get('access_token_cookie')
      user_data = jwt.decode(token, "secret", algorithms=["HS256"])
      new_access_token = jwt.encode({'user': user_data}, 'secret', 'HS256')
      # Set the JWT cookies in the response
      Authorize.set_access_cookies(new_access_token)
      return {"msg":"The token has been refresh"}
    return {'msg': 'There is no refresh_token'}

@app.delete('/logout')
async def logout (Authorize: AuthJWT = Depends()):
    # x = request.cookies.get('access_token_cookie')
    Authorize.unset_jwt_cookies()
    return {"STATUS": "OK"}

@app.get('/protected')
def protected(request: Request, Authorize: AuthJWT = Depends()):
    if check_tokens(request):
      return {"user_id": decode(check_tokens(request))}
    return {'Access is closed'}
