def build_radar(osint_score=None, risk=None, socials=None, ip=None):

    return {
        "labels": ["IP", "Risk", "Socials", "Exposure"],
        "values": [
            20 if ip else 0,
            risk.get("risk_score", 0) if risk else 0,
            len(socials) * 10 if socials else 0,
            osint_score.get("score", 0) if osint_score else 0
        ]
    }