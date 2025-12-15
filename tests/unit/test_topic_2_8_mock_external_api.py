from app.user_service import get_user_name

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("HTTP Error")


def test_get_user_name(monkeypatch):
    def mock_get(url):
        return MockResponse(
            {"id": 1, "name": "Chirag"}
        )
    monkeypatch.setattr(
        "requests.get",
        mock_get
    )
    result = get_user_name(1)
    assert result == "Chirag"
