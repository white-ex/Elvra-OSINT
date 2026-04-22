def build_graph(data):

    nodes = []
    edges = []

    target = data.get("target") or "target"

    ip_data = data.get("ip")
    if ip_data:
        ip_value = ip_data.get("ip") if isinstance(ip_data, dict) else ip_data
        if ip_value:
            nodes.append({"id": "ip", "label": ip_value})
            edges.append({"from": target, "to": "ip"})

    subdomains = data.get("subdomains") or []
    for i, sub in enumerate(subdomains):
        node_id = f"sub_{i}"
        nodes.append({"id": node_id, "label": sub})
        edges.append({"from": "ip", "to": node_id})

    username = data.get("username")
    if username:
        nodes.append({"id": "username", "label": username})
        edges.append({"from": target, "to": "username"})

    email = data.get("email")
    if email:
        nodes.append({"id": "email", "label": email})
        edges.append({"from": target, "to": "email"})

    phone = data.get("phone")
    if phone:
        nodes.append({"id": "phone", "label": phone})
        edges.append({"from": target, "to": "phone"})

    return {
        "nodes": nodes,
        "edges": edges
    }