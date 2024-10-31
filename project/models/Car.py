from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

def create_car(make, model, year, location, status, car_id):
    driver = _get_connection()
    driver.execute_query("CREATE (c:CAR {make:$make, model:$model, year:$year, location:$location, status:$status, car_id:$car_id})",
                         make=make, model=model, year=year, location=location, status=status, car_id=car_id)
    driver.close()

def view_cars():
    driver = _get_connection()
    driver.execute_query('MATCH (c:CAR) RETURN c')
    driver.close()

def update_car(new_make, new_model, new_year, new_location, new_status, new_car_id):
    driver = _get_connection()
    driver.execute_query('''MATCH (c:CAR {car_id:$new_car_id}) SET c.make=$new_make,
                          c.model=$new_model, c.year=$new_year, c.location=$new_location,
                          c.status=$new_status c.car_id=$new_car_id''',
                          new_make=new_make ,new_model=new_model,
                          new_year=new_year, new_location=new_location,
                          new_status=new_status, new_car_id=new_car_id)
    driver.close()

def delete_car(car_id):
    driver = _get_connection()
    driver.execute_query('MATCH (c:CAR {car_id: $car_id}) DETACH DELETE c', car_id=car_id)
    driver.close()
    

class Car:
    def __init__(self, make, model, year, location, status, car_id):
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.status = status
        self.car_id = car_id

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