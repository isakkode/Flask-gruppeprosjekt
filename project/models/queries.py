from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from project.models.Car import _get_connection

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")


def book(carid, customerid):
    car_available = False
    cust_available = False
    bookable = False
    driver = _get_connection() 

    records, summary, keys = driver.execute_query("MATCH (cust:CUSTOMER {customer_id: $cust}) - [p] -> (car:CAR) RETURN cust", cust=customerid)
    if len(records) == 0:
        cust_available = True
    
    records, summary, keys = driver.execute_query("MATCH (cust:CUSTOMER) - [p] -> (car:CAR {car_id: $car}) RETURN car", car=carid)
    if len(records) == 0:
        car_available = True

    if car_available == True and cust_available == True:
        bookable = True

    if bookable == True:
        records, summary, keys = driver.execute_query("""
        MATCH (cust:CUSTOMER {customer_id: $cust}) 
        MATCH (car:CAR {car_id: $car})
        CREATE (cust) - [:BOOKS] -> (car)
        """, car=carid, cust=customerid)

        records, summary, keys = driver.execute_query("""
        MATCH (car:CAR {car_id: $car})
        SET car.status = "Booked"
        """, car=carid)
        driver.close()
        return True
    else:
        driver.close
        return False