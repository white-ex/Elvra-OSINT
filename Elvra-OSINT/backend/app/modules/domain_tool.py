import socket

def analyze_domain(domain):

    if not domain:
        return None

    try:
        ip = socket.gethostbyname(domain)

        return {
            "domain": domain,
            "ip": ip,
            "status": "resolved"
        }

    except:
        return {
            "domain": domain,
            "status": "unresolved"
        }