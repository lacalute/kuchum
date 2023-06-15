from config import *

def user_payload(fname, lname, nick, email, password):
  user = {
    'fname': fname,
    'lname': lname, 
    'nick': nick,
    'email': email, 
    'password': hashing(password),
    'photo': '',
  }
  return user

def post_payload(author, title, content):
  post = {
    "author": author,
    'date': str(datetime.now()).split(' ')[0],
    'title': title,
    'content': content,
    'likes': [],
    'dislikes': [],
    'views': 0,
  }
  return post

def comment_payload(author, content):
  comment = {
    'author': author,
    'date': str(datetime.now()).split(' ')[0],
    'content': content,
    'likes': [],
    'dislikes': []
  }
  return comment

def follower_payload(author, follower):
  follower = {
    'author': author,
    'follower': follower,
  }
  return follower

def subscriber_payload(author, subscriber):
  subscriber = {
    'author': author, 
    'subscriber': subscriber
  }
  return subscriber