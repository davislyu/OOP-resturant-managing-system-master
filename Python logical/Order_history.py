import json
import random
from datetime import datetime
from Data_layer import *


class OrderHistory:
    def __init__(self):
        self.order_history = Data_OrderHistory.get_order_history()

    def print_order_history(self):
        print("Order History:")
        for order in self.order_history['orders']:
            print(f"Order ID: {order['order_id']}, Customer Name: {order['customer_name']}, Total Price: {order['total_price']}, Order Time: {order['order_time']},Table number: {order['table_number']}")

    def edit_order_history(self, order_id, choice, new_value=None):
        order_history = Data_OrderHistory.get_order_history()
        order_to_edit = None
        for order in order_history['orders']:
            if str(order['order_id']) == str(order_id):
                order_to_edit = order
                break
        if order_to_edit:
            if choice == 1:
                order_to_edit['customer_name'] = new_value
            elif choice == 2:
                order_to_edit['total_price'] = new_value
            elif choice == 3:
                items = []
                while True:
                    item_name = input("Enter item name (press q to quit): ")
                    if item_name == 'q':
                        break
                    item_price = float(input("Enter item price: "))
                    item_amount = int(input("Enter item amount: "))
                    items.append({'name': item_name, 'price': item_price, 'amount': item_amount})
                order_to_edit['items'] = items
            elif choice == 4:
                order_to_edit['table_number'] = new_value
                print("The change was made successfully")
            else:
                print("Invalid choice.")
                return
            Data_OrderHistory.save_order_history(order_history)
        else:
            print(f"No order found with ID {order_id}.")
            return

                
    @staticmethod
    def delete_order(order_id):
        order_history = Data_OrderHistory.get_order_history()
        orders = order_history["orders"]

        updated_orders = [
            order for order in orders if order['order_id'] != order_id]

        if len(updated_orders) == len(orders):
            print(f"No order found with ID {order_id}.")
            return

        order_history["orders"] = updated_orders
        Data_OrderHistory.save_order_history(order_history)

        print(f"Order {order_id} has been deleted from the order history.")
        