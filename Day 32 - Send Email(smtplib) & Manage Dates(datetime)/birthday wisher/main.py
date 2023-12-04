import smtplib
from random import randint
import datetime as dt
import pandas as pd

my_email = 'pythontestsmtp100@gmail.com'
password = 'cvkaynjhzegzxlhr'


# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
birthday_data = df.to_dict(orient="records")
birthday_data.extend([birthday for birthday in [
    {'name': 'Subhash', 'email': 'subhashsj227@gmail.com',
        'year': 1999, 'month': 3, 'day': 8},
    {'name': 'Tushar', 'email': 'tushar@gmail.com',
     'year': 1994, 'month': 11, 'day': 20},
    {'name': 'Python', 'email': 'python@gmail.com',
     'year': 1994, 'month': 12, 'day': 4}
] if birthday not in birthday_data])

new_df = pd.DataFrame(birthday_data)
new_df.to_csv("birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

df = pd.read_csv("birthdays.csv")
birthday_data = df.to_dict(orient="records")

for birthday in birthday_data:
    if birthday['month'] == month and birthday['day'] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
            mail_content = letter.read().replace("[NAME]", birthday['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            # tls: Transport Layer Security - making connection secure
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday['email'],
                                msg=f"Subject:Happy Birthday! \n\n {mail_content}")
