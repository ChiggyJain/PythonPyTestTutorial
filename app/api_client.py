import requests

# here request.get is imported at runtime level
def fetch_user(user_id: int) -> dict:
    response = requests.get(f"https://example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()
