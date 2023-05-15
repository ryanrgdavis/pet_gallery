import os
import psycopg2
import psycopg2.extras

DB_URL = os.environ.get("dbname=pet_profile_db")

def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL) # open connection
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use cursor to run SQL commands
    cursor.execute(query, parameters) # begin transaction
    results = cursor.fetchall()
    connection.commit() # end transaction
    connection.close() # close connection
    return results

def create_pet_profile(pet_id, favorite_food, favorite_music, favorite_toys, photo_url):
    sql('INSERT INTO pet_profiles (pet_id, favorite_food, favorite_music, favorite_toys, photo_url) VALUES (%s, %s, %s, %s, %s)', [pet_id, favorite_food, favorite_music, favorite_toys, photo_url])

def create_post(pet_profile_id, user_id, content):
    sql('INSERT INTO posts (pet_profile_id, user_id, content) VALUES (%s, %s, %s)', [pet_profile_id, user_id, content])

def get_all_posts():
    return sql('SELECT * FROM posts ORDER BY created_at DESC')

def create_like(user_id, post_id):
    sql('INSERT INTO likes (user_id, post_id) VALUES (%s, %s)', [user_id, post_id])

def create_comment(user_id, post_id, content):
    sql('INSERT INTO comments (user_id, post_id, content) VALUES (%s, %s, %s)', [user_id, post_id, content])