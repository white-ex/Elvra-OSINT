def explain(osint_score, risk):

    score = osint_score.get("score", 0)

    if score < 30:
        analysis = "Low digital footprint. Minimal public exposure detected."
        level = "SAFE"
    elif score < 70:
        analysis = "Moderate exposure. Some traces exist across public sources."
        level = "MEDIUM"
    else:
        analysis = "High exposure. Multiple digital traces detected across sources."
        level = "HIGH RISK"

    return {
        "analysis": analysis,
        "level": level,
        "technical_note": "Aggregated OSINT signals processed from multiple modules."
    }