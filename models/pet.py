from db.db import sql

def all_pets():
    pets = sql('SELECT * FROM pets ORDER BY pet_id')
    return pets

def get_pet_posts(id):
    if not str(id).isdigit():
        # Handle the error when the id is not an integer
        return "Invalid id. Please enter an integer value."
    id = int(id)
    posts = sql('SELECT * FROM posts WHERE id = %s', [id])
    return posts[0]

def add_pet(pets_name, favourite_food, favourite_music, favourite_toys, image_url):
    sql('INSERT INTO pets (pets_name, favourite_food, favourite_music, favourite_toys, image_url) VALUES (%s, %s, %s, %s, %s) RETURNING *', (pets_name, favourite_food, favourite_music, favourite_toys, image_url))

def delete_pet_post(id):
    sql('DELETE FROM pets WHERE pet_id=%s RETURNING pet_id', [id])

def edit_pet_post(id, pets_name, favourite_food, favourite_music, favourite_toys, image_url):
    sql('UPDATE pets SET pets_name=%s, favourite_food=%s, favourite_music=%s, favourite_toys=%s, image_url=%s WHERE pet_id=%s RETURNING pet_id', (pets_name, favourite_food, favourite_music, favourite_toys, image_url, id))

def create_post(pet_profile_id, user_id, content):
    sql('INSERT INTO posts (pet_profile_id, user_id, content) VALUES (%s, %s, %s)', [pet_profile_id, user_id, content])

def get_all_posts():
    return sql('SELECT * FROM posts ORDER BY created_at DESC')

def create_comment(pet_profile_id, content):
    sql('INSERT INTO comments (pet_profile_id, content) VALUES (%s, %s)', [pet_profile_id, content])