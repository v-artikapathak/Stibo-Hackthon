import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    smtp_server = "smtp.gmail.com"  # Correct SMTP server
    smtp_port = Port no.  # Port for TLS
    sender_email = "Senders email"
    sender_password = "Password"  # Use environment variables for security

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = "Senders Email"
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())

# Example usage
send_email(
    subject="Oracle Reset Process Completed",
    body="The database reset process has been completed successfully.",
    to_email="admin@example.com"
)
