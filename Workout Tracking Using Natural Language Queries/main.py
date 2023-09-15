import requests

APP_ID = "f5a67424"
API_KEY = "73467415749168a0a1e053e934c68118"

user_input = input("What exercise did you perform? ")

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
print(data)