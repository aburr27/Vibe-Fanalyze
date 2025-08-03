-- Vibe-Fanalyze MySQL Schema v1.1

-- SPORTS
CREATE TABLE sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TEAMS
CREATE TABLE teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    abbreviation VARCHAR(10),
    location VARCHAR(100),
    founded_year INT CHECK (founded_year >= 1800),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE
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
    height_cm INT CHECK (height_cm > 0),
    weight_kg INT CHECK (weight_kg > 0),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- SEASONS
CREATE TABLE seasons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    year INT NOT NULL,
    label VARCHAR(50),
    type ENUM('regular', 'playoffs', 'preseason') NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE
);

-- GAMES
CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    season_id INT NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    game_date DATETIME,
    venue VARCHAR(100),
    status ENUM('scheduled', 'in_progress', 'final', 'postponed') DEFAULT 'scheduled',
    final_score_home INT,
    final_score_away INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,
    FOREIGN KEY (season_id) REFERENCES seasons(id) ON DELETE CASCADE,
    FOREIGN KEY (home_team_id) REFERENCES teams(id) ON DELETE CASCADE,
    FOREIGN KEY (away_team_id) REFERENCES teams(id) ON DELETE CASCADE
);

-- PLAYER GAME STATS
CREATE TABLE player_game_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    game_id INT NOT NULL,
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
    FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE,
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- COACHES
CREATE TABLE coaches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sport_id INT NOT NULL,
    team_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role ENUM('head_coach', 'assistant_coach') NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- INJURIES
CREATE TABLE injuries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    team_id INT,
    injury_date DATE,
    description TEXT,
    status ENUM('active', 'questionable', 'doubtful', 'out', 'IR'),
    expected_return DATE,
    FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- GAME EVENTS
CREATE TABLE game_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    timestamp DATETIME NOT NULL,
    event_type VARCHAR(50),
    player_id INT,
    team_id INT,
    description TEXT,
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE SET NULL,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- BETTING LINES
CREATE TABLE betting_lines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    sportsbook VARCHAR(100),
    line_type ENUM('spread', 'moneyline', 'over_under'),
    home_line DECIMAL(6,2),
    away_line DECIMAL(6,2),
    over_under DECIMAL(5,2),
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);
