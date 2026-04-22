def build_query(params: dict):
    parts = []

    if params.get("ip"):
        parts.append(params["ip"])

    if params.get("domain"):
        parts.append(params["domain"])

    if params.get("username"):
        parts.append(params["username"])

    if params.get("location"):
        parts.append(params["location"])

    if params.get("keyword"):
        parts.append(params["keyword"])

    return " ".join(parts)