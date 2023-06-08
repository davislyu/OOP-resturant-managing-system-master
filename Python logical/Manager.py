import json
import random
from datetime import datetime
from Data_layer import *
from Employee import Employee

class Manager(Employee):
    def _init_(self, employee_data):
        super()._init_(employee_data["employee_id"], employee_data["name"],
                         employee_data["phone"], employee_data["email"], employee_data["role"])