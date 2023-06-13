from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from connection import *
import jwt
app = FastAPI()

class Collection:
  def create(self, fname, lname, nick, email, password):
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
    usrs.insert_one(user)
    return str(user['_id'])

  def delete(self, email):
    user = {
      'email': email
    }
  def update(self):
    pass
collection = Collection()

def decode(token):
  decode_token = jwt.decode(token, 'secret', 'HS256')
  return decode_token['id']

def check_tokens(request: Request):
  return request.cookies.get('refresh_token_cookie')


class User(BaseModel):
  fname: str
  lname: str
  nick: str
  email: str
  password: str


class Login(BaseModel):
  nick: str
  password: str

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    # Disable CSRF Protection for this example. default is True
    authjwt_cookie_csrf_protect: bool = False

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
