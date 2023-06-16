from config import *
from tokens import *
from schemes import *
from payloads import comment_payload
crud_posts = CRUD(comments)


@app.post('/create_comment', tags=['posts'])
def create_post(post: Post, req: Request, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, 2, Authorize)
  user_payload = token.decode_token(token.tokens_required(req, 2, Authorize))
  try:
    crud_posts.create(comment_payload(user_payload['user_id'], post.title, post.content))
    return {'msg': 'Post was published'}
  except:
    return {"msg": "Something went wrong"}
  
@app.post('/delete_comment', tags=['posts'])
def delete_post(req: Request, post_id, Authorize: AuthJWT = Depends()):
  token.tokens_required(req, 2, Authorize)
  try:
    crud_posts.delete(post_id)
    return {'msg': 'Post was deleted'}
  except:
    return {'msg':'Something went wrong'}


  
