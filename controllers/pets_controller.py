from flask import render_template, request, redirect
from models.pet import all_pets, get_pet_posts, add_pet, delete_pet_post, create_comment, edit_pet_post, get_comments_for_post
from services.session_info import current_user

def index():
    pets = all_pets()
    user = current_user()
    comments = {}
    for pet in pets:
        pet_posts = get_pet_posts(pet['pet_id'])
        for post in pet_posts:
            comments[post['id']] = get_comments_for_post(post['id'])
    return render_template('pets/index.html', pets=pets, current_user=user, comments=comments)

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

def edit(pet_id):
    pet = get_pet_posts(pet_id)
    return render_template('pets/edit.html', pet=pet)

def update(pet_id):
    pets_name = request.form.get('pets_name')
    favourite_food = request.form.get('favourite_food')
    favourite_music = request.form.get('favourite_music')
    favourite_toys = request.form.get('favourite_toys')
    image_url = request.form.get('image_url')
    edit_pet_post(pet_id, pets_name, favourite_food, favourite_music, favourite_toys, image_url)
    return redirect('/')

def delete(pet_id):
    delete_pet_post(pet_id)
    return redirect('/')

def comment(post_id, content):
    post_id = request.form.get('post_id')
    content = request.form.get('content')
    create_comment(post_id, content)
    return redirect('/pets', post_id=post_id)