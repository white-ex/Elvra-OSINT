def build_profile(username=None, email=None, phone=None, osint_score=None, radar=None, ai=None):

    score = osint_score.get("score", 0) if osint_score else 0
    level = osint_score.get("level", "unknown") if osint_score else "unknown"

    risk_level = ai.get("level", "unknown") if ai else "unknown"
    analysis = ai.get("analysis", "") if ai else ""

    profile_type = "UNKNOWN"

    if score < 30:
        profile_type = "LOW DIGITAL FOOTPRINT"
    elif score < 70:
        profile_type = "MODERATE DIGITAL PRESENCE"
    else:
        profile_type = "HIGH DIGITAL EXPOSURE"

    return {
        "identity": {
            "username": username,
            "email": email,
            "phone": phone
        },

        "digital_profile": {
            "type": profile_type,
            "osint_score": score,
            "level": level
        },

        "risk_assessment": {
            "risk_level": risk_level,
            "summary": analysis
        },

        "radar": radar,

        "recommendation": {
            "security_note": "Reduce exposed data if necessary",
            "privacy_tip": "Avoid reusing same username across platforms"
        }
    }