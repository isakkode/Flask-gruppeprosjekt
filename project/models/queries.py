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
        driver.close()
        return False


def cancel_booking(carid, customerid):
    canbecancelled = False
    driver = _get_connection()

    records, summary, keys = driver.execute_query("MATCH (cust:CUSTOMER {customer_id: $customer}) - [BOOKS] -> (car:CAR {car_id: $car}) RETURN car", car=carid, customer=customerid)
    if len(records) > 0:
        canbecancelled = True
    
    if canbecancelled:
        records, summary, keys = driver.execute_query("MATCH (cust:CUSTOMER {customer_id: $customer}) - [r:BOOKS] -> (car:CAR {car_id: $car}) DELETE r SET car.status = 'Available'", car=carid, customer=customerid)
    driver.close()
    return canbecancelled


def rent_car_query(carid, customerid):
    isbooked = False
    driver = _get_connection()

    records, summary, keys = driver.execute_query("MATCH (c:CUSTOMER {customer_id: $customerid}) - [:BOOKS] -> (c1:CAR {car_id: $carid}) RETURN c, c1", customerid=customerid, carid=carid)
    if len(records) > 0:
        isbooked = True

    if isbooked == True:
            records, summary, keys = driver.execute_query("""MATCH (c:CUSTOMER {customer_id: $customerid}) - [r:BOOKS] -> (c1:CAR {car_id: $carid})
                                                            DELETE r 
                                                            CREATE (c)-[:RENTS]->(c1) 
                                                            SET c1.status = 'Rented'""", customerid=customerid, carid=carid)

    driver.close()
    return isbooked


def return_car_query(carid, customerid, status):
    isrented = False
    driver = _get_connection()

    records, summary, keys = driver.execute_query("MATCH (c:CUSTOMER {customer_id: $customerid}) - [:RENTS] -> (c1:CAR {car_id: $carid}) RETURN c, c1", customerid=customerid, carid=carid)
    if len(records) > 0:
        isrented = True

    if isrented:
        records, summary, keys = driver.execute_query("""MATCH (c:CUSTOMER {customer_id: $customerid}) - [r:RENTS] -> (c1:CAR {car_id: $carid})
                                                      DETACH DELETE r
                                                      SET c1.status = $status""", customerid=customerid, carid=carid, status = status)
        
    driver.close()
    return isrented




