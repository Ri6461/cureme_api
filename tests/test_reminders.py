import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_reminder(async_client):
    response = await async_client.put("/reminders/", json={"message": "Take medication"})
    assert response.status_code == 201
    assert response.json()["message"] == "Take medication"

@pytest.mark.asyncio
async def test_read_reminder(async_client):
    response = await async_client.get("/reminders/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Take medication"

@pytest.mark.asyncio
async def test_update_reminder(async_client):
    response = await async_client.patch("/reminders/1", json={"message": "Updated reminder"})
    assert response.status_code == 200
    assert response.json()["message"] == "Updated reminder"

@pytest.mark.asyncio
async def test_delete_reminder(async_client):
    response = await async_client.delete("/reminders/1")
    assert response.status_code == 204