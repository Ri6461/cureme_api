import pytest
from httpx import AsyncClient
from app.app import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_allergy(async_client: AsyncClient):
    response = await async_client.put("/allergies/", json={"name": "Peanuts"})
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_read_allergy(async_client: AsyncClient):
    response = await async_client.get("/allergies/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Peanuts"


@pytest.mark.asyncio
async def test_update_allergy(async_client: AsyncClient):
    response = await async_client.patch("/allergies/1", json={"name": "Updated Peanuts"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Peanuts" 

@pytest.mark.asyncio
async def test_delete_allergy(async_client: AsyncClient):
    response = await async_client.delete("/allergies/1")
    assert response.status_code == 204






