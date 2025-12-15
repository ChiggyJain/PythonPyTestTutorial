import pytest
from app.async_resource import AsyncResource

# this is async fixture implementation
# here scope default is function level
# Async fixtures allow setup and teardown of async resources
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

# this function is marked as asyncio because
@pytest.mark.asyncio
async def test_async_resource_lifecycle(async_resource):
    assert async_resource.connected is True

