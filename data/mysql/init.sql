-- Vibe-Fanalyze MySQL Schema v1.0

-- SPORTS
CREATE TABLE sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- TEAMS
CREATE TABLE teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    abbreviation VARCHAR(10),
    location VARCHAR(100),
    founded_year INT,
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

-- PLAYERS
CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    team_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(20),
    jersey_number VARCHAR(10),
    birthdate DATE,
    height_cm INT,
    weight_kg INT,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (sport_id) REFERENCES sports(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- SEASONS
CREATE TABLE seasons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT,
    year INT,
    label VARCHAR(50),
    type ENUM('regular', 'playoffs', 'preseason'),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

-- GAMES
CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT,
    season_id INT,
    home_team_id INT,
    away_team_id INT,
    game_date DATETIME,
    venue VARCHAR(100),
    status ENUM('scheduled', 'in_progress', 'final', 'postponed') DEFAULT 'scheduled',
    final_score_home INT,
    final_score_away INT,
    FOREIGN KEY (sport_id) REFERENCES sports(id),
    FOREIGN KEY (season_id) REFERENCES seasons(id),
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id)
);

-- PLAYER GAME STATS
CREATE TABLE player_game_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    game_id INT,
    team_id INT,
    minutes_played DECIMAL(4,1),
    points INT,
    rebounds INT,
    assists INT,
    steals INT,
    blocks INT,
    turnovers INT,
    fouls INT,
    passing_yards INT,
    rushing_yards INT,
    home_runs INT,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- COACHES
CREATE TABLE coaches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT,
    team_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role ENUM('head_coach', 'assistant_coach'),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (sport_id) REFERENCES sports(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- INJURIES
CREATE TABLE injuries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    team_id INT,
    injury_date DATE,
    description TEXT,
    status ENUM('active', 'questionable', 'doubtful', 'out', 'IR'),
    expected_return DATE,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- GAME EVENTS
CREATE TABLE game_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    timestamp DATETIME,
    event_type VARCHAR(50),
    player_id INT,
    team_id INT,
    description TEXT,
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- BETTING LINES
CREATE TABLE betting_lines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    sportsbook VARCHAR(100),
    line_type ENUM('spread', 'moneyline', 'over_under'),
    home_line DECIMAL(6,2),
    away_line DECIMAL(6,2),
    over_under DECIMAL(5,2),
    last_updated DATETIME,
    FOREIGN KEY (game_id) REFERENCES games(id)
);
