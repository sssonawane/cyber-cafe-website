def detect_business(command: str) -> str:
    command = command.lower()

    if "cyber" in command:
        return "Cyber Cafe"
    elif "photo" in command or "studio" in command:
        return "Photo Studio"
    elif "shop" in command or "store" in command:
        return "General Store"
    elif "school" in command:
        return "School / Institute"
    else:
        return "My Business"
