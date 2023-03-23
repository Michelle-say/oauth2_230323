from fastapi import APIRouter, Request, status, Body, File, UploadFile, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel 


router = APIRouter(
    prefix="/login"
)
templates = Jinja2Templates(directory="templates")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login/token")

class User(BaseModel):
    lastname : str = None 
    name : str 
    phone : int
    company : str
    status : str

class NameValues(BaseModel):
    lastname : str = None 
    name : str 
    phone : int
    company : str
    status : str
#Authentification oauth2

@router.get("/", response_class=HTMLResponse)
async def getHome(request: Request):
    return templates.TemplateResponse("login_1.html", {"request": request})


@router.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm =  Depends()):
    print(form_data)
    return {"access_token":form_data.username, "token_type":"bearer"}



@router.get("/users/profilepic")
async def profile_pic(token: str = Depends(oauth_scheme)):
    print(token)
    return {
        "user":"nounou",
        "profile_pic":"my_face"
    }

#Authentification oauth2

@router.post("/postData")
def post_data(name_value: NameValues):
    print(name_value)
    return {
        'name': name_value.name
        }
