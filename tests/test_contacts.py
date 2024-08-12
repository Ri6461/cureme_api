import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_contact(async_client):
    response = await async_client.put("/contacts/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

@pytest.mark.asyncio
async def test_read_contact(async_client):
    response = await async_client.get("/contacts/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

@pytest.mark.asyncio
async def test_update_contact(async_client):
    response = await async_client.patch("/contacts/1", json={"name": "John Smith"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Smith"

@pytest.mark.asyncio
async def test_delete_contact(async_client):
    response = await async_client.delete("/contacts/1")
    assert response.status_code == 204