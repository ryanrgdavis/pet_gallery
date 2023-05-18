from db.db import sql

def all_pets():
    pets = sql('SELECT * FROM pets ORDER BY pet_id')
    return pets

def get_pet_posts(pet_id):
    if not str(pet_id).isdigit():
        # Handle the error when the id is not an integer
        return "Invalid id. Please enter an integer value."
    pet_id = int(pet_id)
    posts = sql('SELECT posts.* FROM posts INNER JOIN pet_profiles ON posts.pet_profile_id = pet_profiles.id WHERE pet_profiles.pet_id = %s', [pet_id])
    return posts

def add_pet(pets_name, favourite_food, favourite_music, favourite_toys, image_url):
    sql('INSERT INTO pets (pets_name, favourite_food, favourite_music, favourite_toys, image_url) VALUES (%s, %s, %s, %s, %s) RETURNING *', (pets_name, favourite_food, favourite_music, favourite_toys, image_url))

def delete_pet_post(pet_id):
    sql('DELETE FROM pets WHERE pet_id=%s RETURNING *', [pet_id])

def edit_pet_post(pet_id, pets_name, favourite_food, favourite_music, favourite_toys, image_url):
    sql('UPDATE pets SET pets_name=%s, favourite_food=%s, favourite_music=%s, favourite_toys=%s, image_url=%s WHERE pet_id=%s RETURNING *', [pets_name, favourite_food, favourite_music, favourite_toys, image_url, pet_id])

def create_post(pet_profile_id, user_id, content):
    sql('INSERT INTO posts (pet_profile_id, user_id, content) VALUES (%s, %s, %s)', [pet_profile_id, user_id, content])

def get_all_posts():
    return sql('SELECT * FROM posts ORDER BY created_at DESC')

def create_comment(post_id, content):
    sql('INSERT INTO comments (pet_id, content) VALUES (%s, %s)', [post_id, content])

def get_comments_for_post(post_id):
    return sql('SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC', [post_id])