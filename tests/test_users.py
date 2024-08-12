import pytest
from httpx import AsyncClient
from app import app  # Assuming your FastAPI app is in app.py

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.put("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

@pytest.mark.asyncio
async def test_read_user(async_client):
    response = await async_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

@pytest.mark.asyncio
async def test_update_user(async_client):
    response = await async_client.patch("/users/1", json={"username": "updateduser"})
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"

@pytest.mark.asyncio
async def test_delete_user(async_client):
    response = await async_client.delete("/users/1")
    assert response.status_code == 204