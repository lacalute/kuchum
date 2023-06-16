from config import *
import time
import jwt
from jwt.exceptions import ExpiredSignatureError

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
    tokens = {
    'refresh': self.tokenRefresh(refresh_token, auth),
    'access': self.tokenAccess(access_token, auth)
    }
    if not access_token and not refresh_token and option != 1:
      raise AccessTokenRequired(status_code=422,message="There are no tokens in cookies")
    return tokens
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
  
  def tokenRefresh(self, refresh_token, Authorize: AuthJWT = Depends()):
    if refresh_token:
      try:
        return jwt.decode(refresh_token, SECRET_KEY, algorithms=ALGORITHM)
      except:
        new_refresh_token = self.create_refresh_token()
        Authorize.set_refresh_cookies(new_refresh_token)
        return jwt.decode(new_refresh_token, SECRET_KEY, algorithms=ALGORITHM)
    
  def tokenAccess(self, access_token, Authorize: AuthJWT = Depends()):
    if access_token:
      try:
        return jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
      except ExpiredSignatureError:
        tokenSplit = access_token.split(".")
        payload = json.loads((base64.b64decode(str(tokenSplit[1]) + "==")).decode("utf-8"))
        new_accesss_token = self.create_access_token(payload['user_id'])
        Authorize.set_access_cookies(new_accesss_token)
        return jwt.decode(new_accesss_token, SECRET_KEY, algorithms=ALGORITHM)
 
token = Token()