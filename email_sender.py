import smtplib
from email.message import EmailMessage

# Sender email and App Password
sender_email = "kolupulathejaswini2706@gmail.com"
app_password = "ssgsowjwknaegxwf"

#Receiver email
receiver_email="vajjalasrihitha09@gmail.com"

# Create email
email = EmailMessage()
email["From"] = sender_email
email["To"] = receiver_email
email["Subject"] = "Test Email from Python"

email.set_content("""
Hello,

i built this Email sender bot using python as part of my syntecxhub internship.

This is a test mail.
Hi ruoooooooo!
How is my test mail?
Had ur dinner?
what ur doing rn?

Thank you!
""")

# Send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, app_password)
        smtp.send_message(email)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)