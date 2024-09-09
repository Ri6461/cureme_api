import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_reminder(async_client):
    response = await async_client.put("/reminders/", json={"message": "Take medication","remind_at": "2022-01-01 08:00:00","id": 5,"user_id": 5})
    assert response.status_code == 201
    assert response.json()["message"] == "Take medication"

@pytest.mark.asyncio
async def test_read_reminder(async_client):
    response = await async_client.get("/reminders/5")
    assert response.status_code == 200
    assert response.json()["message"] == "Take medication"

@pytest.mark.asyncio
async def test_update_reminder(async_client):
    response = await async_client.patch("/reminders/5", json={"message": "Updated reminder"})
    assert response.status_code == 200
    assert response.json()["message"] == "Updated reminder"

@pytest.mark.asyncio
async def test_delete_reminder(async_client):
    response = await async_client.delete("/reminders/5")
    assert response.status_code == 204