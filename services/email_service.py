import smtplib
from email.message import EmailMessage


def send_email(receiver_email, pdf_path):

    sender_email = "vinitaagarwal218@gmail.com"
    sender_password = "qukm lhfq vlts imvk"

    msg = EmailMessage()

    msg["Subject"] = "AI Business Intelligence Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        """
Hello,

Please find attached your AI Business Intelligence Report.

Thank you for using the AI Business Intelligence Platform.

Regards,
AI Business Intelligence Platform
"""
    )

    with open(pdf_path, "rb") as file:
        file_data = file.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="Business_Report.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)