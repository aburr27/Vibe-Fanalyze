-- =====================================================
-- Vibe-Fanalyze Full Database Script
-- Includes tables and sample data
-- =====================================================

-- 1. Create database
DROP DATABASE IF EXISTS vibe_fanalyze;
CREATE DATABASE vibe_fanalyze;
USE vibe_fanalyze;

-- 2. Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Sports table
CREATE TABLE sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- 4. Teams table
CREATE TABLE teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

-- 5. Players table
CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- 6. Games table
CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    game_date DATETIME NOT NULL,
    home_score INT DEFAULT 0,
    away_score INT DEFAULT 0,
    FOREIGN KEY (sport_id) REFERENCES sports(id),
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id)
);

-- 7. Analytics table
CREATE TABLE analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    predicted_winner INT,
    confidence DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(id)
);

-- 8. Bets table
CREATE TABLE bets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id INT NOT NULL,
    bet_type VARCHAR(50),
    amount DECIMAL(10,2),
    placed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (game_id) REFERENCES games(id)
);

-- 1. Insert sample sports
INSERT INTO sports (name) VALUES
('NBA'),('NFL'),('MLB'),('WNBA'),('UFC'),('NHL'),('MLS');

-- 2. Insert sample teams (for simplicity, 2 per sport)
INSERT INTO teams (sport_id, name, city) VALUES
-- NBA
(1, 'Lakers', 'Los Angeles'),(1, 'Bulls', 'Chicago'),
-- NFL
(2, 'Patriots', 'New England'),(2, 'Cowboys', 'Dallas'),
-- MLB
(3, 'Yankees', 'New York'),(3, 'Dodgers', 'Los Angeles'),
-- WNBA
(4, 'Liberty', 'New York'),(4, 'Storm', 'Seattle'),
-- UFC (teams not applicable, we can use gyms/fighters)
(5, 'American Top Team', 'Florida'),(5, 'Jackson Wink MMA', 'New Mexico'),
-- NHL
(6, 'Blackhawks', 'Chicago'),(6, 'Maple Leafs', 'Toronto'),
-- MLS
(7, 'LA Galaxy', 'Los Angeles'),(7, 'Seattle Sounders', 'Seattle');

-- 3. Insert a sample user
INSERT INTO users (username, email, password_hash) VALUES
('AceTester', 'ace@test.com', 'password_hash_here'), -- Replace with actual hashed password
('AceTester2', 'ace2@test.com', 'password_hash_here'), -- Replace with actual hashed password
('FanalyzeUser', 'fanalyze@test.com', 'password_hash_here'); -- Replace with actual hashed password

-- 4. Optional: Insert a sample game
INSERT INTO games (sport_id, home_team_id, away_team_id, game_date) VALUES
(1, 1, 2, '2025-09-10 19:00:00'), -- NBA: Lakers vs Bulls
(2, 2, 1, '2025-09-12 13:00:00'), -- NFL: Cowboys vs Patriots
(1, 2, 1, '2025-09-15 20:00:00'),
(2, 1, 2, '2025-09-20 16:00:00'),
(3, 3, 4, '2025-09-18 19:00:00'),
(4, 4, 3, '2025-09-17 18:00:00'),
(5, 5, 6, '2025-09-19 21:00:00'),
(6, 7, 6, '2025-09-22 19:30:00'),
(7, 8, 7, '2025-09-21 20:00:00');

-- 1. Insert sample analytics for the games
INSERT INTO analytics (game_id, predicted_winner, confidence) VALUES
-- NBA game: Lakers vs Bulls
(1, 1, 75.50),  -- Predicted winner: Lakers, 75.5% confidence
-- NFL game: Cowboys vs Patriots
(2, 2, 62.00),  -- Predicted winner: Patriots, 62% confidence
(3, 2, 68.50),(4, 2, 55.25),(5, 3, 60.00),(6, 4, 70.00),(7, 5, 80.00),(8, 6, 52.75),(9, 7, 65.50);

-- 2. Insert sample bets by the user
INSERT INTO bets (user_id, game_id, bet_type, amount) VALUES
-- User AceTester bets on NBA game
(1, 1, 'Moneyline', 50.00),
-- User AceTester bets on NFL game
(1, 2, 'Spread', 100.00),(1, 3, 'Moneyline', 40.00),(1, 5, 'Over/Under', 75.00),
(2, 4, 'Spread', 50.00),(2, 6, 'Moneyline', 30.00),
(3, 7, 'Spread', 60.00),(3, 9, 'Moneyline', 45.00);
