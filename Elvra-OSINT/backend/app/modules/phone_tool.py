def analyze_phone(phone: str):
    if not phone:
        return None

    phone = phone.replace(" ", "").replace("-", "")

    country = "Unknown"

    if phone.startswith("+33"):
        country = "France"
    elif phone.startswith("+1"):
        country = "USA/Canada"
    elif phone.startswith("+44"):
        country = "UK"

    return {
        "phone": phone,
        "country": country,
        "length": len(phone)
    }