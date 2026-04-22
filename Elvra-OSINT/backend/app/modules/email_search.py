import re

def analyze_email_identity(email: str):

    if not email:
        return None

    email = email.lower().strip()

    result = {
        "email": email,
        "valid_format": False,
        "provider": "unknown",
        "username": None,
        "domain": None,
        "suggestions": []
    }

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if re.match(pattern, email):
        result["valid_format"] = True

    parts = email.split("@")

    if len(parts) == 2:
        username, domain = parts
        result["username"] = username
        result["domain"] = domain

        if "gmail" in domain:
            result["provider"] = "Google"
        elif "outlook" in domain or "hotmail" in domain:
            result["provider"] = "Microsoft"
        elif "yahoo" in domain:
            result["provider"] = "Yahoo"
        else:
            result["provider"] = "Custom domain"

        result["suggestions"] = [
            f"https://www.google.com/search?q=\"{email}\"",
            f"https://www.google.com/search?q=\"{username}\"",
            f"https://github.com/search?q={username}",
            f"https://www.reddit.com/search/?q={username}"
        ]

    return result