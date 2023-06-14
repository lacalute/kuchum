# import all necessary libraries for project
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from connection import *
from fastapi.middleware.cors import CORSMiddleware
import jwt
from http import cookies
morsel = cookies.Morsel()
import time

# init the main FastAPI class
app = FastAPI()


origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

ACCESS_TOKEN_EXPIRE_DELTA = 900.0
REFRESH_TOKEN_EXPIRE_DELTA = 2592000.0
SECRET_KEY = 'secret'
ALGORITHM = 'HS256'

# CRUD users
class CrudUser:
  def __init__(self, fname, lname, nick, email, password):
    user = {
        'fname': fname,
        'lname': lname, 
        'nick': nick,
        'email': email, 
        'password': password,
        'posts': [],
        'followers': [],
        'subscribers': []
      }  
  def create(self):
    usrs.insert_one(self.user)
    return self.user

  def delete(self, email):
    usrs.delete_one(self.user)

  def update(self):
    pass

# CRUD posts
class CrudPosts:
  def __init__(self, title, content):
    post = {
      'title': title,
      'content': content
    }
  
  def create(self):
    pass


class Token():
  # return tokens in cookies
  def get_access_token(self, request: Request):
    try:
      access_token = request.cookies.get('access_token_cookie')
      return access_token
    except:
      return None
    
  def get_refresh_token(self, request: Request):
    try:
      refresh_token = request.cookies.get('refresh_token_cookie')
      return refresh_token
    except:
      return None

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
  
  # return True (if refresh_token is valid) and False (if refresh_token isn't valid)
  def isRefreshToken(self, req: Request, Authorize: AuthJWT = Depends()):
    try:
      try:
        jwt.decode(self.get_refresh_token(req), SECRET_KEY, algorithms=ALGORITHM)
        return True
      except:
        Authorize.set_refresh_cookies(self.create_refresh_token(req))
        return True
    except:
      return False
  
  # return True (if access_token is valid) and False (if access_token isn't valid)
  def isAccessToken(self, request: Request, Authorize: AuthJWT = Depends()):
    try:
      try:
        decode_token = jwt.decode(self.get_access_token(request), SECRET_KEY, algorithms=ALGORITHM)
        return True
      except jwt.ExpiredSignatureError as _ex:
        decode_token = jwt.decode(self.get_access_token(request), "secret", leeway=10.0, algorithms=["HS256"])
        new_accesss_token = self.createToken(decode_token['user_id'])[0]
        Authorize.set_access_cookies(new_accesss_token)
        return True
    except:
      return False
  # return the decoded token
  def decodeToken(self, token):
    return jwt.decode(token, SECRET_KEY, ALGORITHM)


# Scheme for registration
class Registration(BaseModel):
  fname: str
  lname: str
  nick: str
  email: str
  password: str

# Scheme for login
class Login(BaseModel):
  nick: str
  password: str



# AuthJWT class settings
class Settings(BaseModel):
  authjwt_secret_key: str = "secret"
  authjwt_token_location: set = {"cookies"}
  authjwt_cookie_csrf_protect: bool = False

@AuthJWT.load_config
def get_config():
    return Settings()

# error handler
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
