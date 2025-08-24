import pytest
from Presentation import presentation
from Model import models
from fastapi import testclient

client = testclient.TestClient(presentation.router)

@pytest.mark.asyncio
async def test_main_page():
    
    result = client.get("/Decks{}")

    assert result.status_code == 200

@pytest.mark.asyncio
async def test_login():
    
    form_data = {
        "username": "string",
        "password": "password"
    }

    result = client.post("/login", data=form_data)

    assert result.status_code == 200
    assert "access_token" in result.json()
    assert result.json()["token_type"] == "bearer"