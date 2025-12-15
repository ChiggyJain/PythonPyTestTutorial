import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.dependencies import get_current_user


async def override_get_current_user():
    return {
        "id": 1,
        "name": "Chirag",
        "role": "admin"
    }


# Modern FastAPI testing = AsyncClient + ASGITransport
# FastAPI is an ASGI app
# Old-Version of httpx: AsyncClient → app (implicit)
# New-Version of httpx: AsyncClient → ASGITransport → app
@pytest.mark.asyncio
async def test_read_current_user_with_override():
    # here dependency function is overwrite with our own defined function and its happening in memory
    # FastAPI uses override instead of real function
    # Endpoint receives fake user
    # this is [dependency_overrides] inbuilt attributes of fastAPI app object
    app.dependency_overrides[get_current_user] = override_get_current_user
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/me")
    assert response.status_code == 200
    assert response.json()["name"] == "Chirag"
    # here Override cleared from in-memory python process
    app.dependency_overrides.clear()
