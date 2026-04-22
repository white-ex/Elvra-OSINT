import json
from app.modules.osint_engine import full_scan

async def generate_report(target: str):
    data = await full_scan(target)

    report = {
        "target": target,
        "summary": {
            "risk": data["risk"]
        },
        "data": data
    }

    file_path = f"{target}_report.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return {
        "message": "report generated",
        "file": file_path
    }