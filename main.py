import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from routers import HomeRouter, LoginRouter, OupsRouter
import os

app = FastAPI()

app.include_router(LoginRouter.router)
app.include_router(HomeRouter.router)
app.include_router(OupsRouter.router)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")



@app.get("/")
async def redirect():
    return RedirectResponse(url='/login')

if __name__ == '__main__':
    uvicorn.run(
        app,
        port=8080,
        host="0.0.0.0")