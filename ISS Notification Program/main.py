import requests
from datetime import datetime
import smtplib
import time

MY_LAT = LAT # Your latitude
MY_LONG = -LONG # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LAT-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunset_minute = int(data["results"]["sunset"].split("T")[1].split(":")[1])
    # sunset_tuple = (sunset_hour, sunset_minute)

    time_now = datetime.now()
    now_hour = time_now.hour
    now_minute = time_now.minute

    if now_hour >= sunset_hour and now_minute >= sunset_minute:
        if now_hour >= sunset_hour or now_hour <= sunrise:
            return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = "EMAIL"
        password = "PASS"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: The ISS is Now Above You!\n\n"
                    f"Look up to the sky and see if you can see the moving ISS!"
            )
