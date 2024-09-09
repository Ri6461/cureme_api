import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_notification(async_client):
    response = await async_client.put("/notifications/", json={"message": "New notification", "sent_at": "2022-01-01 08:00:00"})
    assert response.status_code == 201
    assert response.json()["message"] == "New notification"

@pytest.mark.asyncio
async def test_read_notification(async_client):
    response = await async_client.get("/notifications/5")
    assert response.status_code == 200
    assert response.json()["message"] == "New notification"

@pytest.mark.asyncio
async def test_update_notification(async_client):
    response = await async_client.patch("/notifications/5", json={"message": "Updated notification"})
    assert response.status_code == 200
    assert response.json()["message"] == "Updated notification"

@pytest.mark.asyncio
async def test_delete_notification(async_client):
    response = await async_client.delete("/notifications/5")
    assert response.status_code == 204