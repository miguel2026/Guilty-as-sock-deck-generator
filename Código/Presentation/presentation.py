from fastapi import APIRouter, Response, Request
from fastapi.responses import HTMLResponse
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
router = APIRouter()


templates = Jinja2Templates(directory="Presentation/templates")

# Docker
@router.get("/HealthCheck", response_class=Response, status_code=200, tags=["Health Check"])
async def Helth_check_Docker():
    return Response(status_code=200)


# Page for the creattion and seeing of the decks
@router.get("/Decks", tags=["Decks"], response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(request,"main_page.html")