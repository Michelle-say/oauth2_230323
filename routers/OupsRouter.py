from fastapi import APIRouter, Request, status, Body, File, UploadFile, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/oups"
)

templates = Jinja2Templates(directory="templates")

@router.get("/oups", response_class=HTMLResponse)
async def getHome(request: Request):
    return templates.TemplateResponse("oups.html", {"request": request})