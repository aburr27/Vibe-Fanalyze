# Vibe-Fanalyze 🎧📊
A multi-sport analytics with chatbot API using FastAPI, MySQL, and MongoDB. and prediction assistant for fans, fantasy players, and stat lovers. Supports NFL, NBA, MLB, WNBA, UFC, NHL, and MLS

Vibe-Fanalyze is a smart multi-sport analytics and prediction assistant for fantasy managers, sports bettors, and stat junkies. It supports:
- 🏈 NFL
- 🏀 NBA
- ⚾ MLB
- 🏀 WNBA
- 🥋 UFC
- 🏒 NHL
- ⚽ MLS

## 🎯 Features
- Player stats lookup
- Team comparisons
- Game schedule queries
- Win/loss predictions
- Fantasy points calculator
- Add/edit/delete sports data
- Chat-like natural language interface
- Betting odds integration

## ⚙️ Tech Stack
- **Backend:** Python (FastAPI or Flask)
- **Database:** MySQL + MongoDB
- **Data Sources:** TheSportsDB, The-Odds-API, etc.
- **Version Control:** GitHub

## 🚀 Getting Started
1. Clone the repo  
   `git clone https://github.com/yourusername/vibe-fanalyze.git`

2. Set up virtual environment  
   `python -m venv venv && source venv/bin/activate` (Linux/Mac)  
   `venv\Scripts\activate` (Windows)

3. Install requirements  
   `pip install -r requirements.txt`

4. Rename `.env.template` to `.env` and fill in your API keys

5. Run the server  
   `python backend/app.py` or `uvicorn backend.app:app --reload`

## 📂 Folder Structure
_See the repo for detailed layout and code organization._

## 📌 License
MIT License

Let’s build something fans *vibe* with.

# Vibe-Fanalyze Project Code Base

## Project Structure
Vibe-Fanalyze/
├── .vscode/
│   └── launch.json
│
├── app/                        # Main application code
│   ├── __init__.py
│   ├── main.py                 # App entry point
│   ├── config/
│   │   └── settings.py
│   ├── db/
│   │   ├── mysql_connector.py
│   │   └── mongodb_connector.py
│   ├── models/
│   │   ├── player.py
│   │   ├── team.py
│   │   └── game.py
│   ├── routes/
│   │   ├── stats.py
│   │   ├── fantasy.py
│   │   ├── games.py
│   │   ├── players.py
│   │   └── teams.py
│   └── services/
│       └── fantasy_points.py
│
├── data/
│   ├── mysql/
│   │   └── init.sql
│   └── mongodb/
│       └── sample_data.json
│
├── scripts/                    # Seeding or utility scripts
│   ├── mysql_seed.py
│   └── mongodb_seed.py
│
├── requirements.txt
├── README.md
└── .gitignore

