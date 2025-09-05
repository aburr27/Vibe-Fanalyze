# Vibe-Fanalyze 🎧📊

A multi-sport analytics with chatbot API using FastAPI, MySQL, and MongoDB. And a prediction assistant for fans, fantasy players, and stat lovers. Supports NFL, NBA, MLB, WNBA, UFC, NHL, and MLS

Vibe-Fanalyze is a smart multi-sport analytics and prediction assistant for fantasy managers, sports bettors, and stat junkies. It supports:

- 🏈 NFL
- 🏀 NBA
- ⚾ MLB
- 🏀 WNBA
- 🥋 UFC
- 🏒 NHL
- ⚽ MLS

## 🎯 Features

- 🔍 Player & team stat lookups
- 📊 Team comparisons
- 🗓️ Game schedule queries
- 🔮 Win/loss predictions
- 🧮 Fantasy points calculator
- ✏️ Add/edit/delete sports data
- 💬 Chat-like interface for natural queries
- 💸 Sports betting odds integration

## ⚙️ Tech Stack

- **Backend:** Python (FastAPI or Flask)
- **Database:** MySQL (structured) + MongoDB (flexible data)
- **Data Sources (planned):** TheSportsDB, The Odds API, etc.
- **Version Control:** Git + GitHub
- **Migrations:** Alembic (MySQL)

## 🚀 Getting Started

1. Clone the repo  
`git clone https://github.com/yourusername/vibe-fanalyze.git`
`cd vibe-fanalyze`

2. Set up virtual environment  
   `python -m venv .venv`
   `python -m venv venv && source venv/bin/activate` (Linux/Mac)  
   `venv\Scripts\activate` (Windows)

3. Install requirements  
   `pip install -r requirements.txt`

4. Rename `.env.template` to `.env` and fill in your API keys

5. Run the server  
   `python backend/app.py` or `uvicorn backend.app:app --reload`

## 📂 Project Structure

Vibe-Fanalyze/

- `.vscode/`                 # IDE configurations
  - `launch.json`
- `app/`                   # Core application
  - `main.py`              # Entry point (runs app)
- `core/`                   # core app setup
  - `app_factory.py`      # create_app() for testing/flexibility
  - `logging.py`          # central logging config
  - `exceptions.py`       # custom error handling
  - `settings.py`        # Environment/configuration management  
- `config/`              # App settings/config
  - `base.py`
  - `dev.py`
  - `prod.py`
  - `settings.py`        # Environment/configuration management
- `db/`                  # DB connectors (MySQL/Mongo)
  - `mysql_connector.py`
  - `mongodb_connector.py`
- `repositories/`           # data access layer
  - `player_repo.py`
  - `team_repo.py`
  - `stats_repo.py`
  - `fantasy_repo.py`
- `models/`              # DB models (SQLAlchemy or ODM)
  - `mlb`
  - `mls`
  - `nba`
    - `player.py`
    - `team.py`
    - `betting.py`
    - `fantasy.py`
    - `stats.py`
    - `game.py`
  - `nfl`
    - `player.py`
    - `team.py`
    - `betting.py`
    - `fantasy.py`
    - `stats.py`
    - `game.py`
  - `nhl`
  - `wnba`
- `schemas/`             # Pydantic schemas
  - `nba`
  - `nfl`
  - `mls`
  - `mlb`
  - `nhl`
  - `wnba`
  - `shared`
- `routes/`              # API endpoints - FastAPI route handlers
  - `v1`                  # versioned
      - `mlb`
      - `mls`
      - `nba`
         - `stats.py`
         - `fantasy.py`
         - `games.py`
         - `players.py`
         - `teams.py`
      - `nfl`
         - `stats.py`
         - `fantasy.py`
         - `games.py`
         - `players.py`
         - `teams.py`
      - `nhl`
      - `wnba`
  - `health.py`           # simple health check endpoint
- `services/`            # Business logic
  - `player_service.py`
  - `team_service.py`
  - `stats_service.py`
  - `betting_service.py`
  - `game_service.py`
  - `fantasy_service.py`
- `utils/`               # Helper functions (optional)
  - `formatter.py`
  - `helper.py`
- `data/`                    # Raw/static data
  - `mysql/`
    - `init.sql`
    - `vibe_fanalyze.sql`
  - `mongodb/`
    - `sample_data.json`
  - `fixtures/`               # static test/seed data
- `migrations`                # Alembic for MySQL schema migrations
- `scripts/`                 # Seeders & CLI tools
  - `mysql_seed.py`
  - `mongodb_seed.py`
- `tests/`                   # Unit/integration tests
  - `conftest.py`
  - `test_players.py`
  - `test_teams.py`
- `env`                     # Local environment config
- `Dockerfile`               # Container setup
- `requirements.txt`         # Python dependencies
- `README.md`
- `.dockerignore`
- `games.stat.json`
- `LICENSE`
- `.gitignore`

## 📌 License

MIT License
Let’s build something fans *vibe* with.
