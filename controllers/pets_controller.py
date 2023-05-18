from flask import render_template, request, redirect, jsonify, url_for
from models.pet import all_pets, add_pet, delete_pet_post, create_comment, edit_pet_post, get_comments_for_pet, get_pet_by_id
from services.session_info import current_user

def index():
    pets = all_pets()
    pets_with_comments = []
    comments = []
    for pet in pets:
        comments = get_comments_for_pet(pet['pet_id'])
        pet['comments'] = comments
        pets_with_comments.append(pet)
    return render_template('pets/index.html', pets=pets_with_comments, current_user=current_user(), comments=comments)

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
    pet = get_pet_by_id(pet_id)
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

def comment(pet_id):
    pet_id = request.form.get('pet_id')
    content = request.form.get('content')
    comments = get_comments_for_pet(pet_id)
    create_comment(pet_id, content)
    pet = get_pet_by_id(pet_id)
    return redirect(url_for('pets_routes.show', pet_id=pet_id, pet=pet, comments=comments, current_user=current_user()))

def show(pet_id):
    pet = get_pet_by_id(pet_id)
    comments = get_comments_for_pet(pet_id)
    return render_template('pets/show.html', pet=pet, comments=comments, current_user=current_user())

# def comment(pet_id):
#     content = request.form.get('content')
#     create_comment(pet_id, content)
#     return redirect('/')

# def toggle_comment(pet_id):
#     show_comments = request.form.get('show_comments')
#     toggle_comments(pet_id, show_comments == 'true')
#     return redirect(url_for('pets_routes.index'))

# def toggle_comment_func(pet_id):
#     show_comments = request.form.get('show_comments')
#     toggle_comments(pet_id, show_comments)
#     return redirect('/pets/index.html', pets=[pet], current_user=current_user())