import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_appointment(async_client):
    response = await async_client.put("/appointments/", json={"date": "2023-10-10", "time": "10:00"})
    assert response.status_code == 201
    assert response.json()["date"] == "2023-10-10"

@pytest.mark.asyncio
async def test_read_appointment(async_client):
    response = await async_client.get("/appointments/1")
    assert response.status_code == 200
    assert response.json()["date"] == "2023-10-10"

@pytest.mark.asyncio
async def test_update_appointment(async_client):
    response = await async_client.patch("/appointments/1", json={"date": "2023-11-11"})
    assert response.status_code == 200
    assert response.json()["date"] == "2023-11-11"

@pytest.mark.asyncio
async def test_delete_appointment(async_client):
    response = await async_client.delete("/appointments/1")
    assert response.status_code == 204