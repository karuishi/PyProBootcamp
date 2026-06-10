##################### SOLUTION ######################
# from datetime import datetime
# import pandas
# import random
# import smtplib

# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )


##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import smtplib, pandas, random
import datetime as dt

my_email = "predelinha@gmail.com"
password = "wdsqcrahrvggnysl"

now = dt.datetime.now()
day = 14
month = 8

birthday_data = pandas.read_csv("birthdays.csv")
# The key is a tuple(month, day) since we want to check only those 2 values
birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in birthday_data.iterrows()}

if (month, day) in birthdays_dict:
    birthday_person = birthdays_dict[(month, day)]
    name = birthday_person["name"]
    email = birthday_person["email"]
    letter_files = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    random_letter = random.choice(letter_files)

    with open(random_letter) as letter:
        content = letter.read()
        new_letter = content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday!\n\n{new_letter}")
else:
    print("no")

