from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.db_mongo import get_recent_chats

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    chats = await get_recent_chats(limit=10)
    return templates.TemplateResponse("chat.html", {"request": request, "chats": chats})

@router.get("/api/chats/recent")
async def recent_chats():
    chats = await get_recent_chats(limit=10)
    for c in chats:
        c["_id"] = str(c["_id"])
    return chats
