def normalize(value):
    if not value:
        return ""
    return str(value).lower().strip()


def similarity(a, b):
    a = normalize(a)
    b = normalize(b)

    if not a or not b:
        return 0

    if a == b:
        return 1

    if a in b or b in a:
        return 0.8

    common = sum(1 for c in a if c in b)
    return common / max(len(a), len(b))


def compute_confidence(username, email, phone, osint_results):

    username = normalize(username)
    email = normalize(email)
    phone = normalize(phone)

    score = 20

    results = osint_results or []

    username_matches = 0

    for r in results:
        u = normalize(r.get("username"))
        sim = similarity(username, u)

        if sim >= 0.8:
            score += 20
            username_matches += 1
        elif sim >= 0.5:
            score += 10
            username_matches += 1

    if email and "@" in email:
        score += 10

    if phone and len(phone) >= 8:
        score += 10

    if len(results) >= 3:
        score += 10

    if username_matches >= 2:
        score += 15

    return min(score, 100)


def build_identity_fusion(username=None, email=None, phone=None, osint_results=None):

    confidence = compute_confidence(username, email, phone, osint_results)

    linked_accounts = []

    for r in osint_results or []:
        u = r.get("username")
        if u:
            linked_accounts.append(normalize(u))

    return {
        "identity": {
            "main_username": username,
            "email": email,
            "phone": phone,
            "linked_accounts": list(set(linked_accounts)),
            "confidence": confidence
        }
    }