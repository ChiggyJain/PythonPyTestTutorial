import pytest
from app.async_resource import AsyncResource

@pytest.fixture
async def async_resource():
    # intitalize the setup with constructor
    resource = AsyncResource()
    # calling async function
    await resource.connect()
    assert resource.connected is True
    yield resource
    # destroying the setup
    await resource.close()

@pytest.mark.asyncio
async def test_async_resource_lifecycle(async_resource):
    assert async_resource.connected is True

