import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_medical_condition(async_client):
    response = await async_client.put("/medical_conditions/", json={"name": "Diabetes"})
    assert response.status_code == 201
    assert response.json()["name"] == "Diabetes"

@pytest.mark.asyncio
async def test_read_medical_condition(async_client):
    response = await async_client.get("/medical_conditions/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Diabetes"

@pytest.mark.asyncio
async def test_update_medical_condition(async_client):
    response = await async_client.patch("/medical_conditions/1", json={"name": "Updated Diabetes"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Diabetes"

@pytest.mark.asyncio
async def test_delete_medical_condition(async_client):
    response = await async_client.delete("/medical_conditions/1")
    assert response.status_code == 204




