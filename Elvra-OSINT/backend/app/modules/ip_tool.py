import requests

def analyze_ip(ip):

    if not ip:
        return None

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()

        return {
            "ip": ip,
            "country": r.get("country"),
            "city": r.get("city"),
            "isp": r.get("isp"),
            "org": r.get("org"),
            "status": r.get("status")
        }

    except:
        return {"ip": ip, "error": "lookup failed"}