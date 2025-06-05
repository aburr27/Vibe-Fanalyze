from fastapi import FastAPI
from backend.routes import stats

app = FastAPI(title="SportsBot API")

app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "Welcome to SportsBot!"}
