import requests
from datetime import datetime as dt
from datetime import timedelta

class FlightSearch: # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.fly_from_IATA_code = "VER"
        self.date = dt.now().date()
        self.KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        
        self.headers = {
            "apikey": "rbcHLv3_zwVjwNeMtBN7ayorEwLoqPYS"
            }

        self.queries = {
            "fly_from": self.fly_from_IATA_code,
            "fly_to": "PARI-sky",
            "date_from": str(self.date),
            "date_to": str(self.date + timedelta(days= 1)),
            "curr": "EUR",
            "one_for_city": 1
        }


    def api_request(self) -> dict:
        endpoint_response = requests.get(url= self.KIWI_ENDPOINT, headers= self.headers, params= self.queries)
        endpoint_response.raise_for_status()
        data = endpoint_response.json()
        return data