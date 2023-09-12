import requests

PIXELA_params = {
    "X-USER-TOKEN": "jk2j1l3lkj13if23f8",
    "username": "notdiego7",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# endpoint_response = requests.post(url= "https://pixe.la/v1/users", json= PIXELA_params)
# print(endpoint_response.json())

endpoint_response = requests.post(url= "https://pixe.la/v1/users/a-know/graphs", json= PIXELA_params)
