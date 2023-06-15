from config import *
import time
import jwt

TokenIsNotThere = JSONResponse(status_code=400, content={'msg': 'There is no token'})

# JWT token config
ACCESS_TOKEN_EXPIRE_DELTA = 900.0
REFRESH_TOKEN_EXPIRE_DELTA = 2592000.0
SECRET_KEY = 'secret'
ALGORITHM = 'HS256'

class Token():
  def tokens_required(self, request, option: Optional[int], auth):
    """
    option - 1 if login or registration
    """
    access_token = request.cookies.get('access_token_cookie')
    refresh_token = request.cookies.get('refresh_token_cookie')
    self.validRefresh(refresh_token, auth)
    self.validAccess(access_token, auth)
    if not access_token and not refresh_token and option != 1:
      raise AccessTokenRequired(status_code=422,message="There are no tokens in cookies")
  
  # return access_token
  def create_access_token(self, user_id):
    access_token = jwt.encode({
      'user_id': user_id,
      'exp': time.time() + ACCESS_TOKEN_EXPIRE_DELTA
    }, SECRET_KEY, algorithm=ALGORITHM)
    return access_token
  
  # return refresh_token
  def create_refresh_token(self):
    refresh_token = jwt.encode({
      'exp': time.time() + REFRESH_TOKEN_EXPIRE_DELTA
    }, SECRET_KEY, algorithm=ALGORITHM)
    return refresh_token
  
  def validRefresh(self, refresh_token, Authorize: AuthJWT = Depends()):
    if refresh_token:
      try:
        jwt.decode(refresh_token, SECRET_KEY, algorithms=ALGORITHM)
      except:
        Authorize.set_refresh_cookies(self.create_refresh_token())
    
  def validAccess(self, access_token, Authorize: AuthJWT = Depends()):
    if access_token:
      try:
        jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
      except:
        decode_token = jwt.decode(access_token, SECRET_KEY, leeway=10.0, algorithms=ALGORITHM)
        new_accesss_token = self.create_access_token(decode_token['user_id'])
        Authorize.set_access_cookies(new_accesss_token)

  def decode_token(self, token):
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
  
token = Token()