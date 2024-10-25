from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from project.models.Car import _get_connection

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")


class Employee:
    def __init__(self, name, address, branch):
        self.name = name
        self.address = address
        self.branch = branch

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
    
    def get_branch(self):
        return self.branch