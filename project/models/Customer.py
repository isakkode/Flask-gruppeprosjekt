from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from project.models.Car import _get_connection

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")

def create_customer(name, age, address, customer_id):
    driver = _get_connection()
    driver.execute_query("CREATE (c:CUSTOMER {name:$name, age:$age, address:$address, customer_id:$customer_id})",
                         name=name, age=age, address=address, customer_id=customer_id)
    driver.close()

def view_customers():
    driver = _get_connection()
    driver.execute_query('MATCH (c:CUSTOMER) RETURN c')
    driver.close()

def update_customer(new_name, new_age, new_address, new_customer_id):
    driver = _get_connection()
    driver.execute_query('''MATCH (c:CUSTOMER {customer_id:$new_customer_id}) 
                            SET c.name=$new_name,
                                c.age=$new_age, 
                                c.address=$new_address 
                            RETURN c''',
                         new_name=new_name, 
                         new_age=new_age,
                         new_address=new_address, 
                         new_customer_id=new_customer_id)
    driver.close()

def delete_customer(customer_id):
    driver = _get_connection()
    driver.execute_query('MATCH (c:CUSTOMER {customer_id: $customer_id}) DETACH DELETE c', customer_id=customer_id)
    driver.close()


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
