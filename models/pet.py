from db.db import sql

def all_pets():
    return sql('SELECT * FROM pets ORDER BY id')

def get_pet_posts(id):
    pet_posts = sql('SELECT * FROM pet_posts WHERE id = %s', [id])
    return pet_posts[0]

def add_pet_post(user_id, pet_id, content, image_url):
    sql('INSERT INTO pet_posts (user_id, pet_id, content, image_url) VALUES (%s, %s, %s, %s) RETURNING *', (user_id, pet_id, content, image_url))

def delete_pet_post(id):
  sql('DELETE FROM pet_posts WHERE id=%s RETURNING *', [id])

def like_pets(pet_id, user_id):
  sql("INSERT INTO likes(user_id, pet_id) VALUES(%s, %s) RETURNING *", [user_id, pet_id])