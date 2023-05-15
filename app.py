from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os
from flask import Flask, redirect
from routes.pets_routes import pets_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
# from routes.profiles_routes import profiles_routes
import requests
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "pretend key for testing only")
print(SECRET_KEY)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(pets_routes, url_prefix='/pets')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')
# app.register_blueprint(profiles_routes, url_prefix='/profiles')

@app.route('/')
def index():
    return redirect('/pets')