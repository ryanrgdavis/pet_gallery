from flask import render_template, request, redirect, session
from models.pet import all_pets, get_pet_posts, add_pet_post, delete_pet_post, like_pets
from services.session_info import current_user

def index():
    pets = all_pets()
    return render_template('pets/index.html', pets=pets, user=current_user())

def new():
    return render_template('pets/new.html')

def add():
    name = request.form.get('name')
    image_url = request.form.get(image_url)
    add_pet_post(name, image_url)
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