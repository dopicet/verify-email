import smtplib
import random

email = input("Enter Your Email: ")
code = ""
for i in range(4):
    code += str(random.randrange(1,9))

def send_code():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yash2003bisht@gmail.com', 'tara@bisht98211')
    server.sendmail('yash2003bisht@gmail.com', email, f"Subject: Verify Your Email\n\n{code}")
    server.close()

try:
    send_code()

except smtplib.SMTPRecipientsRefused:
    print("Invalid email")
    quit()

except Exception:
    print("An error occur!")
    quit()

print("verification code send to your email")
verify_code = input("Enter code: ")
if verify_code == code:
    print("Email verified")
else:
    print("Invalid code")

