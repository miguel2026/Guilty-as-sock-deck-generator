from fastapi import APIRouter, Response, Request
from fastapi.responses import HTMLResponse
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from Model import Models

router = APIRouter()


templates = Jinja2Templates(directory="Presentation/templates")

# Docker
@router.get("/HealthCheck", response_class=Response, status_code=200, tags=["Health Check"])
async def Helth_check_Docker():
    return Response(status_code=200)


# Page for the creattion and seeing of the decks
@router.get("/Decks", tags=["Decks"], response_class=HTMLResponse)
async def main_page(request:Request):

    # enquanto não tem tokens
    user = Models.User(
        id=1,
        username="testuser",
        email="test@email.com",
        password="password123",
        decks=[
            Models.Deck(
                id=1,
                user_id=1,
                name="Test Deck",
                description="A test deck for unit testing.",
                cards=[
                    Models.Card(
                        id=1,
                        deck_id=1,
                        name="Test Card 1",
                        description="This is a test card.",
                        image_url="http://example.com/image1.png"
                    ),
                    Models.Card(
                        id=2,
                        deck_id=1,
                        name="Test Card 2",
                        description="This is another test card.",
                        image_url="http://example.com/image2.png"
                    )
                ]
            )])

    Decks = user.decks
    return templates.TemplateResponse(request,"main_page.html", context={"decks": Decks})




