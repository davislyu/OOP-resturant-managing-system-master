from datetime import datetime
from Data_layer import *


class Employee:
    def __init__(self, employee_id, name, phone, email, role):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.email = email
        self.role = role

    def add_employee(self):
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        employees.append({
            "employee_id": self.employee_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "role": self.role
        })
        Data_Employee.save_employees(employees_data)

    @staticmethod
    def delete_employee(employee_id):
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        for i, employee in enumerate(employees):
            if employee["employee_id"] == employee_id:
                del employees[i]
                break
        Data_Employee.save_employees(employees_data)

    @staticmethod
    def view_employees():
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        print("{:<15} {:<20} {:<15} {:<25} {:<15}".format("employee_id", "name", "phone", "email", "role"))
        for employee in employees:
            phone = employee.get("phone", "")
            email = employee.get("email", "")
            role = employee.get("role", "")  # Get the role value or use an empty string if it is missing
            print("{:<15} {:<20} {:<15} {:<25} {:<15}".format(
                employee["employee_id"], employee["name"], phone, email, role
            ))

    @staticmethod
    def get_employees():
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        return employees
        
    @staticmethod
    def edit_employee(employee_id, field, new_value):
        employees_data = Data_Employee.get_employees()
        employees = employees_data["employees"]
        for employee in employees:
            if employee["employee_id"] == employee_id:
                employee[field] = new_value
                break
        Data_Employee.save_employees(employees_data)