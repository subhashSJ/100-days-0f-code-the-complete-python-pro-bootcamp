import smtplib
from datetime import datetime
from random import choice

my_email = 'pythontestsmtp100@gmail.com'
password = 'cvkaynjhzegzxlhr'

now = datetime.now()
if now.weekday() == 0:
    try:
        with open("quotes.txt") as f:
            quotes = f.readlines()
    except FileNotFoundError:
        quotes = ["No quotes were found"]
        print("File not found")

    with smtplib.SMTP('smtp.gmail.com') as connection:
        # tls: Transport Layer Security - making connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='subhashsj227@gmail.com',
                            msg=f"Subject:Monday Motivation \n\n {choice(quotes)}")
