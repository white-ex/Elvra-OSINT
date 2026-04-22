import httpx

async def get_ip_info(ip: str):
    url = f"http://ip-api.com/json/{ip}"

    async with httpx.AsyncClient() as client:
        data = (await client.get(url)).json()

    return {
        "ip": ip,
        "country": data.get("country"),
        "city": data.get("city"),
        "isp": data.get("isp")
    }