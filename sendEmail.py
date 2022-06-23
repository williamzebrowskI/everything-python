import smtplib, ssl
import getpass

port = 465  # For SSL
password = getpass("Type your password and press enter")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("williamzebrowski7@gmail.com", password)
    # TODO: Send email here

