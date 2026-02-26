import smtplib

def send_email(message):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(
        "tharanishbalaa@gmail.com",
        "APP_PASSWORD"
    )

    server.sendmail(
        "tharanishbalaa@gmail.com",
        "tharanishbalaa@gmail.com",
        message
    )

    server.quit()