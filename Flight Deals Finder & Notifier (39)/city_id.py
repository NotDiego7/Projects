import requests

class CityID: # This class uses a Kiwi endpoint to get the airport IATA Codes for a given city
    def __init__(self):
        self.KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

        self.headers = {
            "apikey": "rbcHLv3_zwVjwNeMtBN7ayorEwLoqPYS",
        }

        self.params = {
            "term": None,
            "location_types": "airport",
            "active_only": True,
        }

    def api_request(self) -> dict:
        print(self.params["term"])
        response = requests.get(self.KIWI_ENDPOINT, headers= self.headers, params= self.params)
        response.raise_for_status()

        data = response.json()
        print(data)

        all_city_IATA_codes = [element["code"] for element in data["locations"]]

        return all_city_IATA_codes
