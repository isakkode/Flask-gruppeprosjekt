from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from project.models.Car import _get_connection

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")




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
