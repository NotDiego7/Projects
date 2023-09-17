import city_id
import data_manager
from flight_search import FlightSearch


data_manager = data_manager.DataManager()
cities = data_manager.api_request_get_cities() #NOTE: This returns all fly_to cities from Sheets
# print(cities)


city_id = city_id.CityID()
object_id = 2 #NOTE: Objects in our sheet start from 2
for city in cities:
    city_id.params["term"] = city
    all_city_IATA_codes = city_id.api_request() #NOTE: This returns all cities IATA Codes (in sequence)

    data_manager.api_request_put_IATAs(all_city_IATA_codes, object_id)

    object_id += 1
    


# data_manager.api_request() #TODO This returns the data from the get request to Sheety

# flight_search = FlightSearch()
# data = flight_search.api_request()
# print(data)