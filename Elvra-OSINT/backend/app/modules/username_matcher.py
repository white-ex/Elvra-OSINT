import re

def normalize(u):
    if not u:
        return ""
    return re.sub(r"[^a-z0-9]", "", str(u).lower())


def similarity(a, b):
    a = normalize(a)
    b = normalize(b)

    if not a or not b:
        return 0

    if a == b:
        return 1.0

    if a in b or b in a:
        return 0.8

    common = sum(1 for c in a if c in b)
    return common / max(len(a), len(b))


def find_similar(username, results):
    if not username:
        return []

    output = []

    for r in results or []:
        u = r.get("username")
        score = similarity(username, u)

        if score >= 0.6:
            output.append({
                "username": u,
                "similarity": round(score, 2),
                "platform": r.get("platform", "unknown"),
                "url": r.get("url", "")
            })

    return sorted(output, key=lambda x: x["similarity"], reverse=True)