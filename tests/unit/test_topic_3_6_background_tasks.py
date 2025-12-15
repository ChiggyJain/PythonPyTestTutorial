import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


class EmailSpy:
    def __init__(self):
        self.called = False
        self.args = None
    async def __call__(self, to: str, subject: str):
        self.called = True
        self.args = (to, subject)


# this function is marked as asyncio
@pytest.mark.asyncio
async def test_background_task_triggered(monkeypatch):
    spy = EmailSpy()
    # here money-patched is happening and replace original-func -> our-testing-func
    monkeypatch.setattr("app.main.send_email", spy)
    transport = ASGITransport(app=app)
    # context manager is happening
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/notify", params={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["status"] == "scheduled"
    assert spy.called is True
    assert spy.args == ("test@example.com", "Welcome!")
