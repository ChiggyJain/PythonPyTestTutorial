
from app.external_service import fetch_exchange_rate


# Direct Import
# here func: fetch_exchange_rate is imported during the import statement and its stored
# into app.currency level as reference level
# Creates a local reference
# Copies fetch_exchange_rate into currency.py
def convert_usd_to_inr(usd_amount: float) -> float:
    rate = fetch_exchange_rate()
    return usd_amount * rate
