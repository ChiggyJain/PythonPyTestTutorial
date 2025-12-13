
from app.currency import convert_usd_to_inr


def test_currency_conversion_with_mock(monkeypatch):
    def mock_fetch_rate():
        return 80.0
    monkeypatch.setattr(
        "app.currency.fetch_exchange_rate",
        mock_fetch_rate
    )
    result = convert_usd_to_inr(2)
    assert result == 160.0
