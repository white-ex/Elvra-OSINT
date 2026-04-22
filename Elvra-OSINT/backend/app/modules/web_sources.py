def get_public_sources(target: str):
    return [
        {
            "title": f"Results about {target}",
            "source": "public_web",
            "snippet": f"Public mentions and references related to {target}."
        },
        {
            "title": f"Technical data for {target}",
            "source": "osint_db",
            "snippet": "No sensitive data, only publicly available references."
        }
    ]