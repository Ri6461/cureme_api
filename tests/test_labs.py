import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_lab(async_client):
    response = await async_client.put("/labs/", json={"name": "Blood test", "result": "Positive", "date": "2022-01-01"})
    assert response.status_code == 201
    assert response.json()["name"] == "Blood test"

@pytest.mark.asyncio
async def test_read_lab(async_client):
    response = await async_client.get("/labs/5")
    assert response.status_code == 200
    assert response.json()["name"] == "Blood test"

@pytest.mark.asyncio
async def test_update_lab(async_client):
    response = await async_client.patch("/labs/5", json={"name": "Updated Blood test"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Blood test"

@pytest.mark.asyncio
async def test_delete_lab(async_client):
    response = await async_client.delete("/labs/5")
    assert response.status_code == 204


