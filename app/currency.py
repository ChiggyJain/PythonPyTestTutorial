
from app.external_service import fetch_exchange_rate


def convert_usd_to_inr(usd_amount: float) -> float:
    rate = fetch_exchange_rate()
    return usd_amount * rate
