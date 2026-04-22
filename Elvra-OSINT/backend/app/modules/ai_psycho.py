def psycho_profile(osint_score, multi):

    score = osint_score.get("score", 0)
    confidence = multi.get("confidence", 0)

    if score < 30:
        profile = "LOW DIGITAL PRESENCE"
        behavior = "User leaves minimal online traces"
    elif score < 70:
        profile = "MODERATE DIGITAL FOOTPRINT"
        behavior = "User has scattered online presence"
    else:
        profile = "HIGH DIGITAL EXPOSURE"
        behavior = "User is highly visible across platforms"

    engagement = "LOW"
    if confidence > 60:
        engagement = "HIGH"

    return {
        "digital_profile": profile,
        "behavioral_analysis": behavior,
        "engagement_level": engagement,
        "note": "This is a statistical OSINT interpretation, not psychological diagnosis"
    }