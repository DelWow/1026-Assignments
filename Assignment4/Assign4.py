'''
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Annas Amar
Student ID: aamar9@uwo.ca
File created: December 9
******************************
This file will process and analyze data about flights and airports. This means like loading data, finding flights based on specific conditions and analizing the durations and if they'll connect.
'''

from Flight import *
from Airport import *

all_airports = {}
all_flights = {}
## I have no idea on how to fix this
def load_data(airport_file, flight_file):
    global all_airports, all_flights
    all_airports = {}
    all_flights = {}

    try:
        with open(airport_file, 'r',) as af:
            for line in af:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('-')
                parts = [p.strip() for p in parts]
                if len(parts) != 3:
                    continue
                code, country, city = parts
                a = Airport(code, city, country)
                all_airports[code] = a

        with open(flight_file, 'r') as ff:
            for line in ff:
                line = line.strip()
                if not line:
                    continue
                raw_parts = line.split('-')
                raw_parts = [p.strip() for p in raw_parts]
                if len(raw_parts) != 5:
                    continue
                flight_no = raw_parts[0] + "-" + raw_parts[1]
                orig_code = raw_parts[2]
                dest_code = raw_parts[3]
                duration_str = raw_parts[4]

                if orig_code not in all_airports or dest_code not in all_airports:
                    continue

                try:
                    duration = float(duration_str)
                except ValueError:
                    continue

                origin_airport = all_airports[orig_code]
                dest_airport = all_airports[dest_code]
                f = Flight(flight_no, origin_airport, dest_airport, duration)

                if orig_code not in all_flights:
                    all_flights[orig_code] = []
                all_flights[orig_code].append(f)

        return True
    except:
        return False


def get_airport_by_code(code):
    # Check if the airport code exists in the collection of all airports
    if code not in all_airports:
        # If not found, raise an error indicating that there is no airport with this code
        raise ValueError(f"No airport with the given code: {code}")
    # Return the airport object associated with the given code
    return all_airports[code]


def find_all_city_flights(city):
    # Initialize an empty list to store flights associated with the given city
    result = []
    # Loop through all the flight lists in the global all_flights dictionary
    for flight_list in all_flights.values():
        # Check each flight in the current flight list
        for flight in flight_list:
            # If the city matches the origin or the destination of the flight
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                # Add the flight to the result list
                result.append(flight)
    # Return the list of all flights related to the specified city
    return result


def find_all_country_flights(country):
    # Initialize an empty list to hold flights related to the given country
    flights = []
    # Iterate through each list of flights in all_flights
    for flight_list in all_flights.values():
        # Check each flight within the list
        for flight in flight_list:
            # If the flight's origin or destination country matches the given country
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                # Add this flight to the result list
                flights.append(flight)
    # Return the listof all flights associated with the specified country
    return flights



def find_flight_between(orig_airport, dest_airport):
    orig_code = orig_airport.get_code()
    dest_code = dest_airport.get_code()

    # Check for direct flight
    if orig_code in all_flights:
        for f in all_flights[orig_code]:
            if f.get_destination() == dest_airport:
                # Return the exact string as required
                return f"Direct Flight: {orig_code} to {dest_code}"

    # If no direct flight, check single-hop
    possible_connections = set()
    if orig_code in all_flights:
        for f in all_flights[orig_code]:
            mid_airport = f.get_destination()
            mid_code = mid_airport.get_code()
            if mid_code in all_flights:
                for f2 in all_flights[mid_code]:
                    if f2.get_destination() == dest_airport:
                        possible_connections.add(mid_code)

    if len(possible_connections) > 0:
        # Return the set of connecting airport codes
        return possible_connections

    # If no direct or single-hop connecting flights
    # Raise ValueError with the exact required message
    raise ValueError(f"There are no direct or single-hop connecting flights from {orig_code} to {dest_code}")


def shortest_flight_from(orig_airport):
    orig_code = orig_airport.get_code()
    if orig_code not in all_flights or len(all_flights[orig_code]) == 0:
        # If there are no flights from this airport, return None or handle as needed
        return None
    shortest_flight = all_flights[orig_code][0]
    shortest_duration = shortest_flight.get_duration()
    for f in all_flights[orig_code]:
        # Compare actual durations without rounding
        if f.get_duration() < shortest_duration:
            shortest_flight = f
            shortest_duration = f.get_duration()
    return shortest_flight

def find_return_flight(first_flight):
    # Iterate over all flights from the detination of the given flight
    for flight in all_flights.get(first_flight.get_destination().get_code(), []):
        # Check if this flight returns to the original departure airport
        if flight.get_destination() == first_flight.get_origin():
            # Returnthe matching return flight if found
            return flight
    # If no matching return flight is found, raise an error
    raise ValueError(f"There is no flight from {first_flight.get_destination().get_code()} to {first_flight.get_origin().get_code()}")
