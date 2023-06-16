from config import *
from payloads import post_payload
from schemes import Post
from tokens import *

crud_posts = CRUD(posts)

@app.post('/create_post', tags=['posts'])
def create_post(post: Post, req: Request, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, 2, Authorize)
  author_payload = token.decode_token(token.tokens_required()[0])
  try:
    crud_posts.create(post_payload(author_payload, post.title, post.content))
    return {'msg': 'Post was published'}
  except:
    return 'Something went wrong'
  
@app.post('/delete_post', tags=['posts'])
def delete_post(post_id):
  try:
    crud_posts.delete(post_id)
    return {'msg': 'Post was deleted'}
  except:
    return 'Something went wrong'

@app.post('/update_post', tags=['posts'])
def update_post(post_id):
  pass

@app.get('/posts', tags=['posts'])
async def all_post():
  return crud_posts.get_all()

@app.get('/post/{post_id}', tags=['posts'])
async def post_id(post_id):
  try:
    return crud_posts.get_id(post_id)
  except:
    return "Post not found"
  

