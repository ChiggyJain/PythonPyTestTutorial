from datetime import datetime
from app.time_service import get_greeting


class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return cls(2025, 1, 1, 9, 0, 0)

def test_morning_greeting(monkeypatch):
    # here datetime-class is replaced with our own class: MockDateTime and MockDateTime is also inherted from datetime
    monkeypatch.setattr(
        "app.time_service.datetime",
        MockDateTime
    )
    assert get_greeting() == "Good Morning"
