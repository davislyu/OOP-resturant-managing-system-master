from Dish import *
from Employee import *
from Hostess import *
from Ingredient import *
from Manager import *
from Menu import *
from Order_history import *
from Order import *
from Stock import Stock
from Table import *
from prototypes import *
from Data_layer import *
from prototypes import PrototypeEmployee, DishPrototype, IngredientPrototype
from Employee import Employee
from Menu import Menu
from Stock import Stock






def handle_add_employee():
    prototype_employee = PrototypeEmployee(
        employee_id=None,
        name=None,
        phone=None,
        email=None,
        role=None
    )

    new_employee = prototype_employee.clone()
    new_employee.get_employee_details_from_input()
    new_employee.add_employee()
    print("Employee added successfully!")


def handle_delete_employee():
    prototype_employee = PrototypeEmployee(
        employee_id=None,
        name=None,
        phone=None,
        email=None,
        role=None
    )

    new_employee = prototype_employee.clone()
    new_employee.get_employee_id_from_input()
    new_employee.delete_employee()
    print("Employee deleted successfully!")


def handle_add_ingredient():
    prototype_ingredient = IngredientPrototype(
        name=None,
        amount=None,
        unit=None
    )

    prototype_ingredient.get_ingredient_details_from_input()

    Stock.add_ingredient(
        name=prototype_ingredient.name,
        amount=prototype_ingredient.amount,
        unit=prototype_ingredient.unit
    )


def handle_add_dish(menu):
    prototype_dish = DishPrototype(
        name=None,
        price=None,
        ingredients=None
    )

    prototype_dish.get_dish_details_from_input()

    new_dish = prototype_dish.clone()
    menu.add_dish(new_dish)
    print(f"{new_dish.name} was added to the menu.")








def handle_view_employees():
    Employee.view_employees()


def handle_print_stock():
    Stock.print_stock()


def handle_view_menu():
    menu = Menu()
    menu.display_menu()






def handle_remove_dish(menu):
    menu.display_menu()
    dish_name = input("Enter the name of the dish you want to remove: ")
    menu.remove_dish(dish_name)


def handle_edit_dish(menu):
    dish_name = input("Enter the name of the dish you want to edit: ")

    for dish in menu.menu_dict['menu_items']:
        if dish['name'] == dish_name:
            print(f"Editing {dish_name}...")
            
            new_name = input(f"Enter a new name for {dish_name} or press Enter to keep {dish_name}: ")
            if new_name.strip():
                dish['name'] = new_name

            new_price_str = input(f"Enter a new price for {dish_name} or press Enter to keep {dish['price']}: ")
            if new_price_str.strip():
                try:
                    new_price = float(new_price_str)
                    dish['price'] = new_price
                except ValueError:
                    print("Invalid input type. Please enter a valid numeric value for the dish price.")

            dish['ingredients'] = []
            while True:
                ingredient_name = input("Enter an ingredient name or 'done' to finish: ")
                if ingredient_name == 'done':
                    break
                ingredient_amount_str = input("Enter the amount of the ingredient: ")
                ingredient_unit = input("Enter the unit of measurement for the ingredient: ")

                if ingredient_name.strip() and ingredient_amount_str.strip():
                    try:
                        ingredient_amount = float(ingredient_amount_str)
                        dish['ingredients'].append({'name': ingredient_name, 'amount': ingredient_amount, 'unit': ingredient_unit})
                    except ValueError:
                        print("Invalid input type. Please enter a valid numeric value for the ingredient amount.")
                else:
                    print("Input cannot be blank. Please enter a valid ingredient name and amount.")

            Data_Menu.save_to_menu(menu.menu_dict)  # Save menu data using the method from Data_layer.py
            print(f"{dish_name} was updated in the menu.")
            break
    else:
        print(f"{dish_name} was not found in the menu.")


def handle_view_order_history(order_history):
    order_history.print_order_history()

def handle_edit_order_history(order_history):
    order_history.print_order_history()
    
    while True:
        order_id = input("Enter the order ID that you want to edit: ")
        if not order_id.strip():
            print("Input cannot be blank. Please try again.")
            continue
        
        try:
            order_id = int(order_id)
            break
        except ValueError:
            print("Invalid input type. Please enter an integer.")
    
    while True:
        try:
            choice = int(input("What do you want to edit? (1=Customer Name, 2=Total Price, 3=Items, 4=Table Number): "))
            break
        except ValueError:
            print("Invalid input type. Please enter an integer.")
    
    if choice == 1:
        new_value = input("Enter the new customer name: ")
        order_history.edit_order_history(order_id, choice, new_value)
    elif choice == 2:
        while True:
            try:
                new_value = float(input("Enter the new total price: "))
                break
            except ValueError:
                print("Invalid input type. Please enter a float.")
        order_history.edit_order_history(order_id, choice, new_value)
    elif choice == 3:
        items = []
        while True:
            item_name = input("Enter item name (press q to quit): ")
            if item_name == 'q':
                break
            while True:
                try:
                    item_price = float(input("Enter item price: "))
                    break
                except ValueError:
                    print("Invalid input type. Please enter a float.")
            while True:
                try:
                    item_amount = int(input("Enter item amount: "))
                    break
                except ValueError:
                    print("Invalid input type. Please enter an integer.")
            items.append({'name': item_name, 'price': item_price, 'amount': item_amount})
        order_history.edit_order_history(order_id, choice, items)
    elif choice == 4:
        while True:
            try:
                new_value = int(input("Enter the new table number: "))
                break
            except ValueError:
                print("Invalid input type. Please enter an integer.")
        order_history.edit_order_history(order_id, choice, new_value)
    else:
        print("Invalid choice.")
        return


def handle_reserve_table():
    tables_data = Data_Table.get_tables()

    print("Tables available for reservation:")
    for table in tables_data['tables']:
        print(Table(table['table_number'], table['status']))

    while True:
        try:
            table_number = int(input("Enter the table number you want to reserve: "))
            break
        except ValueError:
            print("Invalid input type. Please enter an integer.")

    Table.reserve_table(table_number)



def handle_take_order():
    while True:
        customer_name = input("Please enter the customer name: ")

        if not customer_name.strip():
            print("Customer name cannot be blank. Please try again.")
            continue

        break

    table_data = Data_Table.get_tables()

    print("Tables available for reservation:")
    for table in table_data['tables']:
        print(f"Table {table['table_number']}: {table['status']}")

    while True:
        try:
            table_number = int(input("Please enter the table number: "))
            if table_number not in [table['table_number'] for table in table_data['tables']]:
                print("Invalid table number. Please try again.")
                continue

            if table_data['tables'][table_number - 1]['status'] == 'reserved':
                print("Table already reserved. Please choose a different table.")
                continue

        except ValueError:
            print("Invalid input type. Table number should be an integer. Please try again.")
            continue

        break

    menu_data = Data_Menu.display_menu()
    menu_items = menu_data["menu_items"]

    order = Order("", "", "", 0, [])
    order.take_order(customer_name, table_number, menu_items)

    table_data['tables'][table_number - 1]['status'] = 'reserved'
    Data_Table.save_tables(table_data)



def handle_edit_employee():
    employees_data = Data_Employee.get_employees()
    employee_ids = [employee["employee_id"] for employee in employees_data["employees"]]

    Employee.view_employees()

    while True:
        employee_id = input("Enter employee ID (must be a non-empty string): ")

        if not employee_id.strip():
            print("Input cannot be blank. Please try again.")
            continue
        elif employee_id not in employee_ids:
            print("Employee ID not found. Please enter a valid employee ID.")
            continue

        break

    valid_fields = ["name", "phone", "email", "role"]
    field = input("What would you like to edit? (name/phone/email/role): ")

    while field.lower() not in valid_fields:
        print("Invalid choice. Please enter one of the specified options.")
        field = input("What would you like to edit? (name/phone/email/role): ")

    new_value = input("Enter the new value: ")

    while True:
        if not new_value.strip():
            print("Input cannot be blank. Please try again.")
            new_value = input("Enter the new value: ")
            continue

        break

    try:
        employee_id = str(employee_id)
    except ValueError:
        print("Invalid input type for employee ID. Please enter a non-empty string.")

    Employee.edit_employee(employee_id, field, new_value)
    print("Employee updated successfully!")

    
def handle_delete_order(order_history):
    order_history.print_order_history()
    
    while True:
        order_id = input("Enter the ID of the order you would like to delete (must be an integer): ")
        
        if not order_id.strip():
            print("Input cannot be blank. Please try again.")
            continue
        
        try:
            order_id = int(order_id)
            break
        except ValueError:
            print("Invalid input type. Please enter an integer.")
    
    order_history.delete_order(order_id)



def print_menu():
    print("Please select an operation:")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. View Employees")
    print("4. View stock")
    print("5. Add ingredient")
    print("6. Display menu")
    print("7. Add dish")
    print("8. Edit dish")
    print("9. View order history")
    print("10. Edit Order history")
    print("11. Reserve Table")
    print("12. Take an order")
    print("13. remove dish")
    print("14. edit employee")
    print("15. Delete order")
    

def main():
    order_history = OrderHistory()
    menu = Menu()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        

        if choice == "1":
            handle_add_employee()
        elif choice == "2":
            handle_delete_employee()
        elif choice == "3":
            handle_view_employees()
        elif choice == "4":
            handle_print_stock()
        elif choice == "5":
            handle_add_ingredient()
        elif choice == "6":
            handle_view_menu()
        elif choice == "7":
            handle_add_dish(menu)
        elif choice == "8":
            handle_edit_dish(menu)
        elif choice == "9":
            handle_view_order_history(order_history)
        elif choice == "10":
            handle_edit_order_history(order_history)
        elif choice == "11":
            handle_reserve_table()
        elif choice == "12":
            handle_take_order()
        elif choice == "13":
            handle_remove_dish(menu)
        elif choice == "14":
            handle_edit_employee()
        elif choice == "15":
            handle_delete_order(order_history) 

        else:
            print("Invalid choice. Please try again.")

        repeat_action = input("Do you want to perform another action? (yes/no): ")
        if repeat_action.lower() != "yes":
            break


if __name__ == "__main__":
    main()
