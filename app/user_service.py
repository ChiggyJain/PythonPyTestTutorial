from app.api_client import fetch_user


def get_user_name(user_id: int) -> str:
    user = fetch_user(user_id)
    return user["name"]
