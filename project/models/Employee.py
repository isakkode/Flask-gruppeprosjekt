from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from project.models.Car import _get_connection

URI = "neo4j+s://32ed12e3.databases.neo4j.io"
AUTH = ("neo4j", "negOvq9lJfo4gE2zPUjDgqlx309UzNulKCiRWk2x0z8")

def create_employee(name, address, branch, employee_id):
    driver = _get_connection()
    driver.execute_query("CREATE (e:EMPLOYEE {name:$name, address:$address, branch:$branch, employee_id:$employee_id})",
                         name=name, address=address, branch=branch, employee_id=employee_id)
    driver.close()

def view_employees():
    driver = _get_connection()
    driver.execute_query('MATCH (e:EMPLOYEE) RETURN e')
    driver.close()

def update_employee(new_name, new_address, new_branch, new_employee_id):
    driver = _get_connection()
    driver.execute_query('''MATCH (e:EMPLOYEE {employee_id:$new_employee_id}) 
                            SET e.name=$new_name,
                                e.address=$new_address, 
                                e.branch=$new_branch 
                            RETURN e''',
                         new_name=new_name, 
                         new_address=new_address,
                         new_branch=new_branch, 
                         new_employee_id=new_employee_id)
    driver.close()

def delete_employee(employee_id):
    driver = _get_connection()
    driver.execute_query('MATCH (e:EMPLOYEE {employee_id: $employee_id}) DETACH DELETE e', employee_id=employee_id)
    driver.close()

class Employee:
    def __init__(self, name, address, branch):
        self.name = name
        self.address = address
        self.branch = branch
        self.id = id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
    
    def get_branch(self):
        return self.branch