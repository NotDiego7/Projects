from datetime import datetime
import requests

PIXELA_params = {
    "token": "jk2j1l3lkj13if23f8",
    "username": "notdiego7",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# endpoint_response = requests.post(url= "https://pixe.la/v1/users", json= PIXELA_params)
# print(endpoint_response.json())

# ------------------------------ Graph Creation ------------------------------ #
headers = {
    "X-USER-TOKEN": "jk2j1l3lkj13if23f8",
}

# graph_params = {
#     "id": "graph",
#     "name": "Training Record",
#     "unit": "Days",
#     "type": "int",
#     "color": "kuro",
#     "timezone": "America/Mexico_City",
# }

graph_params = {
    "date": f"{datetime.now().date().strftime('%Y%m%d')}",
    "quantity": "1",
}

endpoint_response = requests.put(url= f"https://pixe.la/v1/users/{PIXELA_params['username']}/graphs/graph/{graph_params['date']}", headers= headers, json= graph_params)
print(endpoint_response.text)
