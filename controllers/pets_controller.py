from flask import render_template, request, redirect
from models.pet import all_pets, get_pet_posts, add_pet, delete_pet_post, create_comment, edit_pet_post
from services.session_info import current_user

def index():
    pets = all_pets()
    user = current_user()
    return render_template('pets/index.html', pets=pets, current_user=user)

def new():
    return render_template('pets/new.html')

def add():
    pets_name = request.form.get('pets_name')
    favourite_food = request.form.get('favourite_food')
    favourite_music = request.form.get('favourite_music')
    favourite_toys = request.form.get('favourite_toys')
    image_url = request.form.get('image_url')
    add_pet(pets_name, favourite_food, favourite_music, favourite_toys, image_url)
    return redirect('/')

def edit(id):
    pet = get_pet_posts(id)
    # return render_template('pets/edit.html', pet=pet)
    pets_name = request.form.get('pets_name')
    favourite_food = request.form.get('favourite_food')
    favourite_music = request.form.get('favourite_music')
    favourite_toys = request.form.get('favourite_toys')
    image_url = request.form.get('image_url')
    edit_pet_post(id, pets_name, favourite_food, favourite_music, favourite_toys, image_url)
    return redirect('/', pet=pet)

def delete(id):
    id = delete_pet_post
    delete_pet_post(id)
    return redirect('/')

# def edit(id):
#     pets_name = request.form.get('pets_name')
#     favourite_food = request.form.get('favourite_food')
#     favourite_music = request.form.get('favourite_music')
#     favourite_toys = request.form.get('favourite_toys')
#     image_url = request.form.get('image_url')
#     edit_pet_post(id, pets_name, favourite_food, favourite_music, favourite_toys, image_url)
#     return redirect('/')

def comment(pet_profile_id, content):
    pet_profile_id = request.form.get('pet_profile_id')
    content = request.form.get('content')
    create_comment(pet_profile_id, content)
    return redirect('/pets', pet_profile_id=pet_profile_id)