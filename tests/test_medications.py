import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_medication(async_client):
    response = await async_client.put("/medications/", json={"name": "Aspirin", "dosage": "100mg"})
    assert response.status_code == 201
    assert response.json()["name"] == "Aspirin"

@pytest.mark.asyncio
async def test_read_medication(async_client):
    response = await async_client.get("/medications/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Aspirin"

@pytest.mark.asyncio
async def test_update_medication(async_client):
    response = await async_client.patch("/medications/1", json={"name": "Ibuprofen"})
    assert response.status_code == 200
    assert response.json()["name"] == "Ibuprofen"

@pytest.mark.asyncio
async def test_delete_medication(async_client):
    response = await async_client.delete("/medications/1")
    assert response.status_code == 204