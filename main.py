from fastapi import FastAPI
from backend.routes import stats

app = FastAPI(title="Vibe Fanalyze API")

app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "Welcome to Vibe Fanalyze!"}
