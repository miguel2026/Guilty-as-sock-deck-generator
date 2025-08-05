import pytest
from Presentation import presentation
from Model import Models
from fastapi import testclient

client = testclient.TestClient(presentation.router)

@pytest.mark.asyncio
async def test_main_page():
    
    result = client.get("/Decks")

    assert result.status_code == 200