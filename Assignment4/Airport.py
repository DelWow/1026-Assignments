'''
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Annas Amar
Student ID: aamar9@uwo.ca
File created: December 9
******************************
This file is meant to represent the details about airports. For example, this means comparing airports and updating their attributes (take city and country as an example).
'''

class Airport:
    def __init__(self, code, city, country):
        # Initialize airport attributes
        self._code = code
        self._city = city
        self._country = country

    def __str__(self):
        #Return a formatted string of the airport
        return f"{self._code} ({self._city}, {self._country})"

    def __eq__(self, other):
        # Check airport equality by comparing codes
        if not isinstance(other, Airport):
            return False
        return self._code == other._code

    def get_code(self):
        #Return airport code
        return self._code

    def get_city(self):
        # Return airport city
        return self._city

    def get_country(self):
        #Return airport country
        return self._country

    def set_city(self, city):
        # Set the city
        self._city = city

    def set_country(self, country):
        # Set the country
        self._country = country
