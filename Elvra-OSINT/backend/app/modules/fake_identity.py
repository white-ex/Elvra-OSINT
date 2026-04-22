def detect_fake_identity(multi_search, osint_score):

    confidence = multi_search.get("confidence", 0)
    score = osint_score.get("score", 0)

    risk = "LOW"

    if confidence < 20 and score < 20:
        risk = "SUSPICIOUS IDENTITY"
    elif confidence > 70:
        risk = "LIKELY REAL IDENTITY"
    else:
        risk = "UNCERTAIN"

    return {
        "status": risk,
        "confidence": confidence,
        "score": score
    }