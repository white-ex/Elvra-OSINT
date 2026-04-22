def calculate_risk(ip_data):
    score = 0

    if not ip_data:
        return {"risk_score": 0, "level": "UNKNOWN"}

    if ip_data.get("country"):
        score += 20

    if ip_data.get("city"):
        score += 20

    if ip_data.get("isp"):
        score += 30

    if ip_data.get("country") in ["United States", "Russia", "China"]:
        score += 20

    if score > 100:
        score = 100

    level = "LOW"
    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"

    return {
        "risk_score": score,
        "level": level
    }