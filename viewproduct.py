import tkinter as tk

def update_products():
    # Placeholder function for updating products
    print("Updating products...")

def view_transactions():
    # Placeholder function for viewing transactions
    print("Viewing transactions...")

root = tk.Tk()
root.title("Grocery Store Management")

# Button to update products
update_btn = tk.Button(root, text="Update Products", command=update_products)
update_btn.pack(pady=10)

# Button to view transactions
view_btn = tk.Button(root, text="View Transactions", command=view_transactions)
view_btn.pack(pady=10)

root.mainloop()
#ALSO product listing and create product widgets
import tkinter as tk
from tkinter import ttk

# Dummy data to simulate database records
products = [
    {"ID": 1, "category": "Groceries", "Item_name": "Bread", "cost": 2.50, "no_of_items": 20},
    {"ID": 2, "category": "Groceries", "Item_name": "Milk", "cost": 1.75, "no_of_items": 30},
    {"ID": 3, "category": "Groceries", "Item_name": "Eggs", "cost": 3.00, "no_of_items": 50}
]

def add_to_cart(product_id, cost):
    # Placeholder function to handle adding the product to the cart
    print(f"Product ID: {product_id}, Cost: {cost} added to cart")

def create_product_widgets():
    for product in products:
        product_frame = ttk.Frame(root)
        product_frame.pack(fill=tk.X, padx=10, pady=5)

        label = ttk.Label(product_frame, text=f"Product ID: {product['ID']}, Category: {product['category']}, Item Name: {product['Item_name']}, Cost: {product['cost']}, No. of Items: {product['no_of_items']}")
        label.pack(side=tk.LEFT)

        add_button = ttk.Button(product_frame, text="Add to Cart", command=lambda p_id=product['ID'], c=product['cost']: add_to_cart(p_id, c))
        add_button.pack(side=tk.RIGHT)

root = tk.Tk()
root.title("Grocery Store Products")

# Header
header_frame = ttk.Frame(root)
header_frame.pack(fill=tk.X)

cart_button = ttk.Button(header_frame, text="View your cart")
cart_button.pack(side=tk.LEFT, padx=10, pady=5)

user_button = ttk.Button(header_frame, text="User Profile")
user_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Logo
logo_frame = ttk.Frame(root)
logo_frame.pack(fill=tk.X)

logo_label = ttk.Label(logo_frame, text="Grocery Store", font=("Helvetica", 24))
logo_label.pack(padx=10, pady=5)

# Product List
product_list_frame = ttk.Frame(root)
product_list_frame.pack()

# Product Table
create_product_widgets()

root.mainloop()