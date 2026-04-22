import requests

def check_username(username: str):
    if not username:
        return []

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "X": f"https://x.com/{username}"
    }

    results = []

    for platform, url in sites.items():
        try:
            r = requests.get(url, timeout=3)
            exists = r.status_code == 200
        except:
            exists = False

        results.append({
            "platform": platform,
            "url": url,
            "exists": exists
        })

    return results