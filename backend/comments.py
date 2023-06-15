from config import *
from tokens import *
from schemes import *
from payloads import comment_payload
crud_posts = CRUD(comments)


@app.post('/create_comment', tags=['posts'])
def create_post(post: Post, req: Request, Authorize: AuthJWT = Depends()):
  if token.isAccessToken(req, Authorize) and token.isRefreshToken(req, Authorize):
    user_payload = token.decodeToken(token.get_access_token(req))
    print(user_payload)
    try:
      crud_posts.create(comment_payload(user_payload, post.title, post.content))
      return {'msg': 'Post was published'}
    except:
      return 'Something went wrong'
  
@app.post('/delete_comment', tags=['posts'])
def delete_post(post_id):
  try:
    crud_posts.delete(post_id)
    return {'msg': 'Post was deleted'}
  except:
    return 'Something went wrong'


  
