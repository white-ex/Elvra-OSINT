def scrape_osint(username):

    results = []

    platforms = ["GitHub", "Reddit", "X", "TikTok"]

    for p in platforms:
        results.append({
            "platform": p,
            "query": username,
            "found": False
        })

    return results