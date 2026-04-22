from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from app.modules.osint_engine import full_scan
from app.modules.ai_summary import generate_summary


async def generate_pdf(target: str):

    data = await full_scan(target)
    summary = generate_summary(data)

    file_path = f"{target}_report.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("TraceScope X - OSINT Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Target: {target}", styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("AI Summary", styles["Heading2"]))
    elements.append(Paragraph(summary, styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Identity Fusion", styles["Heading2"]))
    elements.append(Paragraph(str(data.get("identity_fusion")), styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("OSINT Score", styles["Heading2"]))
    elements.append(Paragraph(str(data.get("osint_score")), styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Similar Accounts", styles["Heading2"]))
    elements.append(Paragraph(str(data.get("similar_accounts")), styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Graph Data", styles["Heading2"]))
    elements.append(Paragraph(str(data.get("graph")), styles["Normal"]))

    doc.build(elements)

    return file_path