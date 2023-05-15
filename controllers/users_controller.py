from flask import render_template, request, redirect
from models.user import create_user, create_pet_profile

def new():
  return render_template('users/new.html')

def add():
  first_name = request.form.get('first_name')
  last_name = request.form.get('last_name')
  email = request.form.get('email')
  password = request.form.get('password')
  create_user(first_name, last_name, email, password)
  return redirect('/')

def add_pet():
  pet_id = request.form.get("Name: ")
  favourite_food = request.form.get("Favourite Food: ")
  favourite_music = request.form.get("Favourite Music: ")
  favourite_toys = request.form.get("Favourite Toys: ")
  image_url = request.form.get("Image URL: ")
  ('INSERT INTO pet_profiles (pet_id, favourite_food, favourite_music, favourite_toys, image_url) VALUES (%s, %s, %s, %s, %s)', [pet_id, favourite_food, favourite_music, favourite_toys, image_url])