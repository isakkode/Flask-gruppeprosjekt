from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver


class Car:
    def __init__(self, make, model, year, location, status):
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.status = status

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_location(self):
        return self.location

    def set_location(self, value):
        self.location = value
    
    def get_status(self):
        return self.status
    
    def set_status(self, value):
        self.status = value