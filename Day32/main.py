# import smtplib

my_email = "predelinha@gmail.com"
friend_email = "pedrolucas.js18@gmail.com"
password = "wdsqcrahrvggnysl"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # encrypts the msg 
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="pedrolucas.js18@gmail.com", 
        # msg="Subject:Hello\n\nThis is the body of my email."
#         )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# date_of_birth = dt.datetime(year=2001, month=8, day=14, hour=12)
# print(now)
# print(year)
# print(month)
# print(day_of_week)
# print(date_of_birth)

import smtplib, random
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()

if weekday == weekday:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=friend_email, 
            msg=f"Subject:{weekday} Motivation\n\n{quote}".encode('utf-8')
        )
        