from datetime import datetime


def get_greeting() -> str:
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good Morning"
    elif current_hour < 18:
        return "Good Afternoon"
    return "Good Evening"
