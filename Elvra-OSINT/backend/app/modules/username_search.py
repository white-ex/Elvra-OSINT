import requests

def search_username(username):

    sites = {
        # Social
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Instagram": "https://www.instagram.com/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Twitter/X": "https://twitter.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",

        # Dev
        "GitLab": "https://gitlab.com/{}",
        "Bitbucket": "https://bitbucket.org/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",

        # Gaming
        "Steam": "https://steamcommunity.com/id/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Xbox": "https://xboxgamertag.com/search/{}",

        # Creative
        "Pinterest": "https://www.pinterest.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "Medium": "https://medium.com/@{}",
        "Behance": "https://www.behance.net/{}",

        # Forums
        "Quora": "https://www.quora.com/profile/{}",
        "Pastebin": "https://pastebin.com/u/{}",

        # Crypto / misc
        "AboutMe": "https://about.me/{}",
        "Linktree": "https://linktr.ee/{}"
    }

    results = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for platform, url in sites.items():

        full_url = url.format(username)

        try:
            r = requests.get(full_url, headers=headers, timeout=3)

            if r.status_code == 200:
                results.append({
                    "platform": platform,
                    "url": full_url,
                    "username": username
                })

        except:
            pass

    return results