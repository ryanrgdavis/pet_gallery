CREATE DATABASE pet_profile_db;
\c pet_profile_db 

CREATE TABLE pets( 
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    image_url TEXT 
); 

INSERT INTO pets(name, image_url)
VALUES 
    ('Mary', '');

CREATE TABLE users( 
    id SERIAL PRIMARY KEY, 
    first_name TEXT, 
    last_name TEXT, 
    email TEXT 
); 

ALTER TABLE users ADD COLUMN password_digest TEXT; 

CREATE TABLE likes( 
    id SERIAL PRIMARY KEY, 
    user_id INTEGER, 
    pet_id INTEGER 
);

CREATE TABLE pet_profiles(
    id SERIAL PRIMARY KEY,
    pet_id INTEGER REFERENCES pets(id),
    favorite_food TEXT,
    favorite_music TEXT,
    favorite_toys TEXT,
    photo_url TEXT
);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    pet_profile_id INTEGER REFERENCES pet_profiles(id),
    user_id INTEGER REFERENCES users(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    post_id INTEGER REFERENCES posts(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);