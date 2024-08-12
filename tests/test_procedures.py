import pytest
from httpx import AsyncClient
from app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_procedure(async_client):
    response = await async_client.put("/procedures/", json={"name": "Surgery"})
    assert response.status_code == 201
    assert response.json()["name"] == "Surgery"

@pytest.mark.asyncio
async def test_read_procedure(async_client):
    response = await async_client.get("/procedures/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Surgery"

@pytest.mark.asyncio
async def test_update_procedure(async_client):
    response = await async_client.patch("/procedures/1", json={"name": "Updated Surgery"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Surgery"

@pytest.mark.asyncio
async def test_delete_procedure(async_client):
    response = await async_client.delete("/procedures/1")
    assert response.status_code == 204


