import re

def analyze_email(email: str):
    if not email:
        return None

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    valid = bool(re.match(pattern, email))

    domain = email.split("@")[-1] if "@" in email else None

    providers = {
        "gmail.com": "Google",
        "outlook.com": "Microsoft",
        "hotmail.com": "Microsoft",
        "yahoo.com": "Yahoo"
    }

    return {
        "email": email,
        "valid_format": valid,
        "domain": domain,
        "provider": providers.get(domain, "Unknown")
    }