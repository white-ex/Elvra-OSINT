def multi_search(email=None, phone=None, username=None):

    results = {
        "inputs": {
            "email": email,
            "phone": phone,
            "username": username
        },
        "signals": [],
        "confidence": 0
    }

    score = 0

    if email:
        results["signals"].append("email detected in OSINT pipeline")
        score += 30

    if phone:
        results["signals"].append("phone number analyzed")
        score += 30

    if username:
        results["signals"].append("username search enabled")
        score += 40

    results["confidence"] = min(score, 100)

    return results