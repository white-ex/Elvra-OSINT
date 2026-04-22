def search_socials(username: str):
    if not username:
        return []

    platforms = [
        {"platform": "GitHub", "url": f"https://github.com/{username}"},
        {"platform": "Twitter/X", "url": f"https://x.com/{username}"},
        {"platform": "Instagram", "url": f"https://instagram.com/{username}"},
        {"platform": "Reddit", "url": f"https://reddit.com/user/{username}"},
        {"platform": "TikTok", "url": f"https://tiktok.com/@{username}"},
        {"platform": "LinkedIn", "url": f"https://www.linkedin.com/in/{username}"}
    ]

    return platforms