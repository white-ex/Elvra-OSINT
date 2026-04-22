def compute_global_score(ip=None, risk=None, socials=None):

    score = 0

    if risk and isinstance(risk, dict):
        score += risk.get("risk_score", 0)

    if socials:
        score += len(socials) * 5

    if ip:
        score += 10

    if score > 100:
        score = 100

    if score < 40:
        level = "low"
        message = "Low digital footprint"
    elif score < 70:
        level = "medium"
        message = "Moderate online presence"
    else:
        level = "high"
        message = "High online exposure"

    return {
        "score": score,
        "level": level,
        "message": message
    }