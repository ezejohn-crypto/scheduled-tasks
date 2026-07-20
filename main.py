##################### Normal Starting Project ######################
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import pandas
from datetime import datetime
birthday_data = pandas.read_csv('birthdays.csv')
now = datetime.now()
today = (now.month, now.day)
birth_dict = {(row['month'], row['day']): row for (index, row) in birthday_data.iterrows()}


# # Email credentials
# sender_email = "godstimemacaulay@gmail.com"
# sender_password = "orowvtphwsvktlau"  # Use an app password if required

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")



if today in birth_dict:
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
        messagee = file.read()
        person = birth_dict[today]
        email_person = birth_dict[today]
        birthday_message = messagee.replace('[NAME]', person['name'])
        print(birthday_message)

        # Create the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email_person['email']
        message["Subject"] = "Happy Birthday!!!"

        body = f"Hello,\n\n{birthday_message}.\n\nRegards"
        message.attach(MIMEText(body, "plain"))

        # Send the email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Encrypt the connection
                server.login(sender_email, sender_password)
                server.send_message(message)

            print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")





