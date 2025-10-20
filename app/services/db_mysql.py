"""
MySQL Database Connection for Vibe-Fanalyze
Stores structured prediction and bankroll analytics.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

MYSQL_URI = os.getenv("MYSQL_URI", "mysql+pymysql://root:password@localhost/vibefanalyze")

engine = create_engine(MYSQL_URI)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    team_a = Column(String(100))
    team_b = Column(String(100))
    favorite = Column(String(100))
    underdog = Column(String(100))
    win_probability = Column(Float)
    bet_size = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def save_prediction_log(data: dict):
    """Save a prediction or Kelly analysis result."""
    session = SessionLocal()
    record = PredictionLog(
        team_a=data.get("team_a"),
        team_b=data.get("team_b"),
        favorite=data.get("favorite"),
        underdog=data.get("underdog"),
        win_probability=data.get("probability") or data.get("win_prob_a"),
        bet_size=data.get("bet_size")
    )
    session.add(record)
    session.commit()
    session.close()
