import requests
from datetime import datetime

APP_ID = "f5a67424"
API_KEY = "73467415749168a0a1e053e934c68118"
SHEETY_AUTH = "Basic ZGllZ28wMDdsb3BlekBnbWFpbC5jb206RnVja2FsbHRoYXRsYW1lc2hpdA=="

user_input = input("What exercise did you perform? ")

# ------------------------- Get Current Time and Date ------------------------ #
curr_datetime = datetime.now()

curr_date = curr_datetime.date().strftime("%B %d, %Y")
curr_time = curr_datetime.time().strftime("%#I:%M")

# ------------------------------ Nutritionix API ----------------------------- #
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 60.0,
    "age": 26
}

endpoint_response = requests.post(url= "https://trackapi.nutritionix.com/v2/natural/exercise", headers= headers, json= params)
endpoint_response.raise_for_status()
data = endpoint_response.json()
# print(data["exercises"])

# -------------------------------- Sheety API -------------------------------- #
headers = {
    "Authorization": SHEETY_AUTH
}

for i in range(len(data["exercises"])):
    params = {
        "workout": {
            "date": curr_date,
            "time": curr_time,
            "exercise": data["exercises"][i]["name"].title(),
            "duration": float(data["exercises"][i]["duration_min"]),
            "calories": data["exercises"][i]["nf_calories"]
        }
    }

    endpoint_response = requests.post(url= "https://api.sheety.co/1a84f2e650fc7bc0e7234c4555b6d5ad/myWorkouts/workouts", headers= headers, json= params)
    endpoint_response.raise_for_status()
    print(endpoint_response.text)

    #FIXME: Duration appears wrong on the Spreadsheet but is right on script and API.text return...