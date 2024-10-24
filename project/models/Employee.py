from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://8ec87af7.databases.neo4j.io"
AUTH = ("neo4j", "U25elaIO30nL4UxJuC7Qi-S0tn8GmemiS3whj2UORUQ")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

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
    

