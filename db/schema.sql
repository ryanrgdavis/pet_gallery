CREATE DATABASE pet_profile_db;
\c pet_profile_db 

CREATE TABLE pets( 
    pet_id SERIAL PRIMARY KEY,
    pets_name TEXT,
    favourite_food TEXT,
    favourite_music TEXT,
    favourite_toys TEXT,
    image_url TEXT 
); 

INSERT INTO pets(pets_name, favourite_food, favourite_music, favourite_toys, image_url)
VALUES 
    ('Mary', 'Chicken', 'Meow - lvusm', 'Fishing Rod', 'https://i.ibb.co/6swm5Y0/IMG-1320.jpg');
    ('Mei Mei & Delilah', 'Rice', 'Bulgarian Song & Dance', 'The birds outside', 'https://i.ibb.co/ftfjSgd/bcf0b020-4f14-4fc3-9927-5696eeb94ad3.jpg')

CREATE TABLE users( 
    id SERIAL PRIMARY KEY, 
    first_name TEXT, 
    last_name TEXT, 
    email TEXT,
); 

ALTER TABLE users ADD COLUMN password_digest TEXT; 

CREATE TABLE pet_profiles(
    id SERIAL PRIMARY KEY,
    pet_id INTEGER REFERENCES pets(id),
    pets_name TEXT,
    favourite_food TEXT,
    favourite_music TEXT,
    favourite_toys TEXT,
    image_url TEXT
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