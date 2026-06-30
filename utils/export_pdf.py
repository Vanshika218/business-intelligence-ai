from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report, filename="Business_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []
    for line in report.split("\n"):
        line = line.replace("₹", "Rs.")
        story.append(Paragraph(line, styles["Normal"]))
    doc.build(story)

    return filename