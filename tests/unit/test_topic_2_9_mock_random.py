from app.random_service import roll_dice

def test_roll_dice(monkeypatch):
    def mock_randint(a, b):
        return 4
    monkeypatch.setattr(
        "random.randint",
        mock_randint
    )
    assert roll_dice() == 4
