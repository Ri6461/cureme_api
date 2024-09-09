import pytest
from httpx import AsyncClient
from app import app  # Assuming your FastAPI app is in app.py

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.put("/users/", json={ "email": "test@example.com", "first_name": "Test", "last_name": "User", "dob": "1990-01-01", "phone_number": "1234567890", "address": "123 Main St","secret": "password", "created_at": "2022-01-01T00:00:00", "updated_at": "2022-01-01T00:00:00" })
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

@pytest.mark.asyncio
async def test_read_user(async_client):
    response = await async_client.get("/users/5")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

@pytest.mark.asyncio
async def test_update_user(async_client):
    response = await async_client.patch("/users/5", json={"email": "rit@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "rit@example.com"

@pytest.mark.asyncio
async def test_delete_user(async_client):
    response = await async_client.delete("/users/5")
    assert response.status_code == 204