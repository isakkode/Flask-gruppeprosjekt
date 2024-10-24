from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://8ec87af7.databases.neo4j.io"
AUTH = ("neo4j", "U25elaIO30nL4UxJuC7Qi-S0tn8GmemiS3whj2UORUQ")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age =  age
        self.address = address 

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_address(self):
        return self.address
