from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status

class AppException(Exception):
def __init__(self, name: str, detail: str):
self.name = name
self.detail = detail

def app_exception_handler(request: Request, exc: AppException):
return JSONResponse(
status_code=status.HTTP_400_BAD_REQUEST,
content={"error": exc.name, "detail": exc.detail},
)