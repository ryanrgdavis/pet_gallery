from flask import render_template, request, redirect, session
from models.pet import all_pets, get_pet_posts, add_pet, delete_pet_post, like_pets
from services.session_info import current_user

def index():
    pets = all_pets()
    user = current_user()
    return render_template('pets/index.html', pets=pets, current_user=user)

def new():
    return render_template('pets/new.html')

def add():
    pet_id = request.form.get('pet_id')
    favourite_food = request.form.get('favourite_food')
    favourite_music = request.form.get('favourite_music')
    favourite_toys = request.form.get('favourite_toys')
    image_url = request.form.get('image_url')
    add_pet(pet_id, favourite_food, favourite_music, favourite_toys, image_url)
    return redirect('/')

def edit(id):
    pet = get_pet_posts(id)
    return render_template('pets/edit.html', pet=pet)

def delete(id):
    delete_pet_post(id)
    return redirect('/')

def like(id):
    like_pets(id, session ['user_id'])
    return redirect('/')