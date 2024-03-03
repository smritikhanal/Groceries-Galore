import tkinter as tk
from tkinter import messagebox
import mysql.connector
 
def process():
    cpid = cpid_entry.get()
 
    # Connect to MySQL database
    conn = mysql.connector.connect(host='localhost', user='root', password='12345', database='grocery_store')
    cursor = conn.cursor()
 
    # Query cart table to get the number of items for the given product ID
    cursor.execute("SELECT quantity FROM cart WHERE product_id=%s", (cpid,))
    row1 = cursor.fetchone()
    cart_count = row1[0] if row1 else 0
   
    # Query products table to get the current number of items for the given product ID
    cursor.execute("SELECT quantity FROM products WHERE product_ID=%s", (cpid,))
    row2 = cursor.fetchone()
    product_count = row2[0] if row2 else 0
   
    # Calculate the new count by adding the cart count to the product count
    new_count = cart_count + product_count
   
    # Update the products table with the new count
    cursor.execute("UPDATE products SET quantity=%s WHERE product_ID=%s", (new_count, cpid))
   
    # Delete the record from the cart table
    cursor.execute("DELETE FROM cart WHERE product_id=%s", (cpid,))
   
    # Commit changes to the database
    conn.commit()
   
    # Close cursor and connection
    cursor.close()
    conn.close()