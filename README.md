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
- **Data Sources:** TheSportsDB, The Odds API, and more
- **Version Control:** Git + GitHub

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

## 📂 Project Structure
Vibe-Fanalyze/
├── .vscode/                 # IDE configurations
│    └── launch.json
├── app/                     # Core application
│   ├── app.py               # FastAPI app instance (create_app)
│   ├── main.py              # Entry point (runs app)
│   ├── config/              # App settings/config
│   │    └── settings.py      # Environment/configuration management
│   ├── db/                  # DB connectors (MySQL/Mongo)
│   │  ├── mysql_connector.py
│   │  └── mongodb_connector.py
│   ├── models/              # DB models (SQLAlchemy or ODM)
│   │   ├── player.py
│   │   ├── team.py
│   │   └── game.py
│   ├── schemas/             # Pydantic schemas
│   ├── routes/              # API endpoints - FastAPI route handlers
│   │   ├── stats.py
│   │   ├── fantasy.py
│   │   ├── games.py
│   │   ├── players.py
│   │   └── teams.py
│   ├── services/            # Business logic
│       └── fantasy_points.py
│   └── utils/               # Helper functions (optional)
│      └── formatter.py
├── data/                    # Raw/static data
│   ├── mysql/
│      └── init.sql
│   └── mongodb/
│       └── sample_data.json
├── scripts/                 # Seeders & CLI tools
│   ├── mysql_seed.py
│   └── mongodb_seed.py
├── tests/                   # Unit/integration tests
│   ├──conftest.py
│   ├──test_players.py
│   ├── test_teams.py
├── .env                     # Local environment config
├── Dockerfile               # Container setup
├── requirements.txt         # Python dependencies
├── README.md
├── .dockerignore
├── games.stat.json
├── LICENSE
└── .gitignore
└── ...                      # Other config and metadata files

## 📌 License
MIT License

Let’s build something fans *vibe* with.
