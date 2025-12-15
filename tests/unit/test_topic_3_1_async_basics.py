import pytest
from app.async_math import add_async


# here event loop will be managed automatically by pytest
# (Starts event loop -> Executes async function -> Awaits coroutine -> Validates assertion)
@pytest.mark.asyncio
async def test_add_async():
    result = await add_async(2, 3)
    assert result == 5
