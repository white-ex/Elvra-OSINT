import httpx
import asyncio

SITES = {
    "github": "https://github.com/{}",
    "reddit": "https://www.reddit.com/user/{}",
    "twitter": "https://twitter.com/{}",
    "instagram": "https://instagram.com/{}"
}

async def check_username(site, url):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(url)

            if r.status_code == 200:
                return site
    except:
        pass

    return None


async def scan_username(username: str):
    tasks = []

    for site, url in SITES.items():
        tasks.append(check_username(site, url.format(username)))

    results = await asyncio.gather(*tasks)

    return {
        "username": username,
        "found_on": [r for r in results if r]
    }