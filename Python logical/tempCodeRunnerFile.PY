def handle_edit_order_history(order_history):
    order_history.print_order_history()
    order_id = input("Enter the order ID that you want to edit: ")
    choice = int(input("What do you want to edit? (1=Customer Name, 2=Total Price, 3=Items, 4=Table Number): "))

    if choice == 1:
        new_value = input("Enter the new customer name: ")
        order_history.edit_order_history(order_id, choice, new_value)
    elif choice == 2:
        new_value = float(input("Enter the new total price: "))
        order_history.edit_order_history(order_id, choice, new_value)
    elif choice == 3:
        items = []
        while True:
            item_name = input("Enter item name (press q to quit): ")
            if item_name == 'q':
                break
            item_price = float(input("Enter item price: "))
            item_amount = int(input("Enter item amount: "))
            items.append({'name': item_name, 'price': item_price, 'amount': item_amount})
        order_history.edit_order_history(order_id, choice, items)
    elif choice == 4:
        new_value = int(input("Enter the new table number: "))
        order_history.edit_order_history(order_id, choice, new_value)
    else:
        print("Invalid choice.")
        return