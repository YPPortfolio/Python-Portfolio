##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import smtplib


# --- ADD NEW BIRTHDAYS TO THE CSV FILE ---#

with open("birthdays.csv", "r") as birthdays_file:
    birthdays_data = pd.read_csv(birthdays_file)
    existing_birthdays_list = birthdays_data.to_dict(orient="list")

    new_birthdays = pd.DataFrame(
        {"name": ["Jason", "Carmen", "Thomas", "Jimmy", "Shawn"],
         "email": ["peacenlov32@gmail.com", "peacenlov32@gmail.com", "peacenlov32@gmail.com",
                   "peacenlov32@gmail.com", "peacenlov32@gmail.com"],
         "year": ["1961", "1961", "1961", "1961", "1961"],
         "month": ["2", "2", "2", "2", "2"],
         "day": ["9", "11", "15", "13", "14"],
         }
    )
    new_birthdays_list = new_birthdays.to_dict(orient="list")

    for name in new_birthdays_list["name"]:
        if name not in existing_birthdays_list["name"]:
            addition = new_birthdays.loc[new_birthdays["name"] == name]
            birthdays_data = birthdays_data.append(addition)
        else:
            pass
    birthdays_data.to_csv("birthdays.csv", index=False)



# --- CHECK IF TODAY MATCHES A DATE IN CSV ---#
today = dt.datetime.now()
month = today.month
day = today.day

with open("birthdays.csv", "r") as birthdays_file:
    birthdays_file_data = pd.read_csv(birthdays_file)
    birthdays_dict = birthdays_file_data.to_dict(orient="dict")

    today_birthday = birthdays_file_data[(birthdays_file_data.day == day)
                              & (birthdays_file_data.month == month)].to_dict(orient="list")
    today_birthday_name = today_birthday["name"][0]

with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
    letter = letter_file.read()
    updated_letter = letter.replace("[NAME]", today_birthday_name)


#--- Send Letter as Email ---#
my_email = "peacenlov32@gmail.com"
password = "atyflgvppcjsahyh"

today_birthday_email = today_birthday["email"][0]

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=today_birthday_email,
        msg=f"Subject: Happy Birthday!!!\n\n"
            f"{updated_letter}"
    )
