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

    elements.append(Paragraph("OSINT REPORT", styles["Title"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Target: " + target, styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Summary:", styles["Heading2"]))
    elements.append(Paragraph(summary or "No data", styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Identity:", styles["Heading2"]))
    elements.append(Paragraph(str(data.get("identity_fusion", {})), styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Score:", styles["Heading2"]))
    elements.append(Paragraph(str(data.get("osint_score", 0)), styles["Normal"]))

    doc.build(elements)

    return file_path