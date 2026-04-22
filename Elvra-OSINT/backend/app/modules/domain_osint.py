import socket
import httpx

async def get_domain_info(domain: str):

    ip = socket.gethostbyname(domain)

    async with httpx.AsyncClient() as client:
        res = await client.get(f"http://{domain}", timeout=5)
        headers = dict(res.headers)

    return {
        "domain": domain,
        "ip": ip,
        "headers": headers
    }