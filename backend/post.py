from config import *


@app.post('/create_post', tags=['posts'])
def create_post(post: Post, req: Request, Authorize: AuthJWT = Depends()):
  if token.isAccessToken(req, Authorize) and token.isRefreshToken(req, Authorize):
    user_payload = token.decodeToken(token.get_access_token(req))['user_id']
    print(user_payload)
    try:
      crud_post.create_post(user_payload, post.title, post.content)
      return {'msg': 'Post was published'}
    except:
      return 'Something went wrong'
  

@app.post('/delete_post', tags=['posts'])
def delete_post(post_id):
  try:
    crud_post.delete_post(post_id)
    return {'msg': 'Post was deleted'}
  except:
    return 'Something went wrong'

@app.get('/posts', tags=['posts'])
async def all_post():
  all_posts = []
  for post in posts.find():
    post['_id'] = str(post['_id'])
    all_posts.append(post)
  return all_posts

@app.get('/post/{id}', tags=['posts'])
async def post_id(id):
  try:
    post_id = posts.find_one({'_id': ObjectId(id)})
    post_id['_id'] = str(post_id['_id'])
    return post_id
  except:
    return "Post not found"