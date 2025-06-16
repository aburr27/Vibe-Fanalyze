CREATE DATABASE IF NOT EXISTS vibe_fanalyze;

USE vibe_fanalyze;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    favorite_league VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE leagues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    sport_type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS favorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    type ENUM('player', 'team'),
    reference_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);



