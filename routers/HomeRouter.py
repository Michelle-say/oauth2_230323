from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/home"
)
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def getHome(request: Request):
    return templates.TemplateResponse("home_2.html", {"request": request})