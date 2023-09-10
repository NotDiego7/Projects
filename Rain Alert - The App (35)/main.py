import requests, smtplib

# API_KEY = "bd5e378503939ddaee76f12ad7a97608" Key for OpenWeather
LATITUDE = 19.929359
LONGITUDE = -96.852966

parameters = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "apparent_temperature_max,precipitation_sum,precipitation_probability_max",
    "temperature_unit": "fahrenheit",
    "timezone": "auto",
    "forecast_days": 1,
}

end_point_response = requests.get(url="https://api.open-meteo.com/v1/forecast", params= parameters)
end_point_response.raise_for_status()
data = end_point_response.json()

precipitation_mm = data["daily"]["precipitation_sum"][0]
apparent_temperature_max = data["daily"]["apparent_temperature_max"][0]
precipitation_probability_max = data["daily"]["precipitation_probability_max"][0]
daily_weather_data = f"Temperatura Máxima (Sensación): {apparent_temperature_max}°F\nProbabilidad Máxima de Lluvia: {precipitation_probability_max}%\nMilímetros de Lluvia: {precipitation_mm}mm"

# ------------------------- Send Email to SMS Gateway ------------------------ #

carriers = {
	'att':      '@mms.att.net',
	'tmobile':  '@tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com',
    'telcel':   '@itelcel.com',
}

def send(message):
    # Encode the message as UTF-8; Else, ASCII encode error arises
    message = message.encode('utf-8')

    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = '2351078070@itelcel.com'
    auth = ("Diego007lopez@gmail.com", "grxdhlzlwiflpyru")

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)

send(daily_weather_data)