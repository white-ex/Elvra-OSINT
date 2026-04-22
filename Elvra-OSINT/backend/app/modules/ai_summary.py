def generate_summary(data):

    score = data.get("osint_score", {}).get("score", 0)
    risk = data.get("risk", {}).get("risk_score", 0)

    if score < 30:
        presence = "very limited online presence"
    elif score < 70:
        presence = "moderate online activity"
    else:
        presence = "strong and consistent digital presence"

    if risk < 30:
        risk_text = "low exposure risk"
    elif risk < 70:
        risk_text = "moderate exposure risk"
    else:
        risk_text = "high exposure risk"

    return f"""
This profile indicates {presence}.
The analyzed data suggests a {risk_text} based on available OSINT signals.
Patterns show that the subject maintains a detectable footprint across public sources.
"""