from fastapi import APIRouter
from app.modules.osint_engine import full_scan
from app.modules.identity_osint import search_identity

router = APIRouter()

@router.get("/graph/{target}")
async def graph(target: str):
    data = await full_scan(target)
    identity = search_identity(target)

    nodes = []
    edges = []

    nodes.append({"id": target, "label": target})

    if data.get("ip"):
        ip = data["ip"]["ip"]
        nodes.append({"id": ip, "label": ip})
        edges.append({"from": target, "to": ip})

    for sub in data.get("subdomains") or []:
        nodes.append({"id": sub, "label": sub})
        edges.append({"from": target, "to": sub})

    for profile in identity.get("profiles"):
        pid = profile["platform"] + ":" + profile["username"]
        nodes.append({"id": pid, "label": pid})
        edges.append({"from": target, "to": pid})

    return {"nodes": nodes, "edges": edges}