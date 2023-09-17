import requests


class DataManager: # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/1a84f2e650fc7bc0e7234c4555b6d5ad/flightDeals/prices"
        self.headers = {"Authorization": "Basic ZGllZ28wMDdsb3BlekBnbWFpbC5jb206RnVja2FsbHRoYXRsYW1lc2hpdA=="}
        # self.queries = {
        #     "price": {
        #         "iataCode": "VER"
        #     }
        # }
    
    def api_request_get_cities(self) -> list:
        endpoint_response = requests.get(url= self.SHEETY_ENDPOINT, headers= self.headers)
        endpoint_response.raise_for_status()
        data = endpoint_response.json()
        
        cities = [element["city"] for element in data["prices"]]
        return cities

    def api_request_put_IATAs(self, IATA_codes, object_id) -> list:
        print(object_id)
        IATA_codes = ', '.join(IATA_codes)
        queries = {
            "price": {
                "iataCode": IATA_codes
            }
        }

        endpoint_response = requests.put(url= f"{self.SHEETY_ENDPOINT}/{object_id}", headers= self.headers, json= queries)
        endpoint_response.raise_for_status()
        print(endpoint_response.text)