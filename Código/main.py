from fastapi import FastAPI
from Presentation import presentation

API = FastAPI(
    title="Guilty as Sock deck generator",
    description="A simple API to generate decks for the Guilty as Sock card game.",
    version="0.2.0"
)

API.include_router(presentation.router)
