from app.id_service import generate_id


def test_generate_id(monkeypatch):
    class MockUUID:
        @staticmethod
        def uuid4():
            return "fixed-uuid-123"
    monkeypatch.setattr(
        "app.id_service.uuid",
        MockUUID
    )
    assert generate_id() == "fixed-uuid-123"
