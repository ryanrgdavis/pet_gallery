from db.db import sql

def all_pets():
    pets = sql('SELECT * FROM pets ORDER BY pet_id')
    return pets

def get_pet_posts(id):
    pet_posts = sql('SELECT * FROM pet_posts WHERE id = %s', [id])
    return pet_posts[0]

def add_pet(pet_id, favourite_food, favourite_music, favourite_toys, image_url):
    sql('INSERT INTO pets (pet_id, favourite_food, favourite_music, favourite_toys, image_url) VALUES (%s, %s, %s, %s, %s) RETURNING *', (pet_id, favourite_food, favourite_music, favourite_toys, image_url))

def delete_pet_post(id):
  sql('DELETE FROM pet_posts WHERE id=%s RETURNING *', [id])

def like_pets(pet_id, user_id):
  sql("INSERT INTO likes(user_id, pet_id) VALUES(%s, %s) RETURNING *", [user_id, pet_id])

def create_post(pet_profile_id, user_id, content):
    sql('INSERT INTO posts (pet_profile_id, user_id, content) VALUES (%s, %s, %s)', [pet_profile_id, user_id, content])

def get_all_posts():
    return sql('SELECT * FROM posts ORDER BY created_at DESC')

def create_like(user_id, post_id):
    sql('INSERT INTO likes (user_id, post_id) VALUES (%s, %s)', [user_id, post_id])

def create_comment(user_id, post_id, content):
    sql('INSERT INTO comments (user_id, post_id, content) VALUES (%s, %s, %s)', [user_id, post_id, content])