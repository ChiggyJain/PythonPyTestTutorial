import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app


# Modern FastAPI testing = AsyncClient + ASGITransport
# FastAPI is an ASGI app
# Old-Version of httpx: AsyncClient → app (implicit)
# New-Version of httpx: AsyncClient → ASGITransport → app
@pytest.mark.asyncio
async def test_health_check_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# Modern FastAPI testing = AsyncClient + ASGITransport
# FastAPI is an ASGI app
# Old-Version of httpx: AsyncClient → app (implicit)
# New-Version of httpx: AsyncClient → ASGITransport → app
@pytest.mark.asyncio
async def test_add_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5


