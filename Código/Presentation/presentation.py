from fastapi import APIRouter, Response, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from Workflow import services
import jwt


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
templates = Jinja2Templates(directory="Presentation/templates")

# Docker
@router.get("/HealthCheck", response_class=Response, status_code=200, tags=["Health Check"])
async def Helth_check_Docker():
    return Response(status_code=200)


# Page for the creattion and seeing of the decks
@router.get("/Deck/{id}", tags=["Decks"], response_class=HTMLResponse)
async def main_page(request:Request, id: int, token: Annotated[str, Depends(oauth2_scheme)] = None):
    
    user_id = services.id_from_token(token)
    user = services.fake_user(user_id)

    # Enquanto não tem banco de dados
    Deck = user.decks[0]
    return templates.TemplateResponse(request,"main_page.html", context={"deck": Deck})


@router.post("/login", tags=["Authentication"])
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):

    user = services.fake_user(services.id_from_name(form.username))

    if not user:
        print("User not found")
        return HTTPException(404, detail="Invalid credentials")
    
    hashed_pass = services.hash_password(form.password)
    
    if not services.verify_password(form.password, user.password):
        print("Not the same password")
        return HTTPException(404, detail="Invalid credentials")
    else:
        token = services.create_access_token(user.model_dump())
        return token


@router.post("/sign_up", tags=["Authentication"])
async def sign_up(request:Request):
    pass


