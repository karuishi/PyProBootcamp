import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"
sheet_updated = False

for row in sheet_data:
    if row["iataCode"] == "" or row["iataCode"] == "TESTING":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # Slowing down requests to avoid rate limit
        time.sleep(2)
        sheet_updated = True
        
if sheet_updated:
    print(f"sheet_data: {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
else:
    print("No missing IATA codes found. Sheet is up to date!")
    
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    
    if cheapest_flight.price != "N/A":
        if cheapest_flight.price < destination["lowestPrice"]:
            print(f"Lower price flight found to {destination['city']}! Updating sheet...")
            data_manager.update_lowest_price(row_id=destination["id"], new_price=cheapest_flight.price)
            
    # Slowing down requests to avoid rate limit
    time.sleep(2)