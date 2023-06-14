from config import *


@app.post('/create_post', tags=['posts'])
def create_post():
  pass

@app.post('/delete_post', tags=['posts'])
def delete_post():
  pass

@app.get('/post/{id}')
async def post_id(id):
  pass
