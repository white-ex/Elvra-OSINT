def get_verdict(risk_score: int):
    if risk_score is None:
        return {"level": "unknown", "message": "No data available"}

    if risk_score < 40:
        return {"level": "safe", "message": "Low digital exposure detected"}
    elif risk_score < 70:
        return {"level": "medium", "message": "Moderate online presence"}
    else:
        return {"level": "high", "message": "High exposure detected on public sources"}