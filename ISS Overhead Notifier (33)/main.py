import requests, smtplib
from datetime import datetime
from time import sleep

MY_LAT = 19.918112
MY_LONG = -96.852115

# ----------------------------- GET ISS grid data ---------------------------- #

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# --- Check if my position is within +5 or -5 degrees of the ISS position. --- #

if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:

    # ------------------------------- GET Sun Data ------------------------------- #

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
    }

    sun_endpoint_response = requests.get("https://api.sunrisesunset.io/json", params= parameters)
    sun_endpoint_response.raise_for_status()
    sun_dict = sun_endpoint_response.json()
    sunrise_time = sun_dict["results"]["sunrise"]
    sunset_time = sun_dict["results"]["sunset"]

    # ---------- Convert Sunrise and Sunset Times to 24hr Format And Int --------- #

    sunrise_time_obj = datetime.strptime(sunrise_time, '%I:%M:%S %p')
    sunset_time_obj = datetime.strptime(sunset_time, '%I:%M:%S %p')

    sunrise_time_24hr = int(sunrise_time_obj.strftime('%H:%M:%S')[:-6])
    sunset_time_24hr = int(sunset_time_obj.strftime('%H:%M:%S')[:-6])

    current_time = datetime.now().time().hour

    # ---------------------------- Check if NightTime ---------------------------- #
    
    if current_time > sunset_time_24hr and current_time < sunrise_time_24hr:
        with smtplib.SMTP(host= "smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login("Diego007lopez@gmail.com", "grxdhlzlwiflpyru")
            connection.sendmail(from_addr= "Diego007lopez@gmail.com", to_addrs= "Lopez.d9@outlook.com", msg= f"Subject: ISS Overhead Alert\n\nThe International Space Station is currently overhead.\nISS Latitude: {iss_latitude}\nISS Longitude: {iss_longitude}")
        
        # --------------------------- Run every 60 seconds --------------------------- #

        sleep(secs=20.0)