-- Initialize MySQL Database for Vibe-Fanalyze
CREATE DATABASE IF NOT EXISTS vibe_fanalyze;
USE vibe_fanalyze;


CREATE TABLE IF NOT EXISTS players (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
team VARCHAR(50) NOT NULL
);