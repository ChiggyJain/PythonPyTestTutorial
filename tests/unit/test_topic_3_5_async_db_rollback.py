import pytest
from app.fake_async_db import FakeAsyncDBSession


# this is async fixture implementation
# here scope default is function level
# Async fixtures allow setup and teardown of async resources
@pytest.fixture
async def db_session():
    session = FakeAsyncDBSession()
    await session.begin()   # START TRANSACTION
    yield session           # TEST RUNS HERE
    await session.rollback()  # ROLLBACK


# this function is marked as asyncio and used async-fixture
@pytest.mark.asyncio
async def test_db_insert_isolated(db_session):
    await db_session.insert({"id": 1, "name": "Chirag"})
    assert len(db_session.data) == 1

