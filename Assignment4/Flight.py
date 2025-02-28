'''
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Annas Amar
Student ID: aamar9@uwo.ca
File created: December 9
******************************
The purpose of this flight file is meant to represent the details of flights, checking on attributes about the flight for example, duration and type (if its international or domestic), and to combine flights which are possible to combine.
'''

from Airport import *

class Flight:
    def __init__(self, flight_no, origin, dest, dur):
        # Validate that origin and dest are Airport objects, then set attributes
        if not isinstance(origin, Airport) or not isinstance(dest, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        self._flight_no = flight_no
        self._origin = origin
        self._destination = dest
        self._duration = dur

    def __str__(self):
        # Return a string with flight info and domestic/international status
        dur_rounded = round(self._duration)
        flight_type = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({dur_rounded}h) [{flight_type}]"

    def __eq__(self, other):
        # Check if other is a Flight and both origin and destination match
        if not isinstance(other, Flight):
            return False
        return (self._origin == other._origin) and (self._destination == other._destination)

    def __add__(self, conn_flight):
        # Validate connection and return a new Flight with combined duration
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        if self.get_destination() != conn_flight.get_origin():
            raise ValueError("These flights cannot be combined")
        return Flight(
            flight_no=self.get_flight_no(),
            origin=self.get_origin(),
            dest=conn_flight.get_destination(),
            dur=self.get_duration() + conn_flight.get_duration()
        )

    def get_flight_no(self):
        # Return flight number
        return self._flight_no

    def get_origin(self):
        # Return origin Airport object
        return self._origin

    def get_destination(self):
        # Return destination Airport object
        return self._destination

    def get_duration(self):
        # Return flight duration
        return self._duration

    def is_domestic(self):
        # Return True if origin and destination are in the same country
        return self._origin.get_country() == self._destination.get_country()

    def set_origin(self, origin):
        # Set the origin Airport object
        self._origin = origin

    def set_destination(self, destination):
        # Set the destination Airport object
        self._destination = destination
