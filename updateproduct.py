import tkinter as tk
from tkinter import messagebox
import mysql.connector

def update_product():
    product_id = product_id_entry.get()
    name = name_entry.get()
    category = category_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='grocery_store',
                                             user='root',
                                             password='sagarme')

        cursor = connection.cursor()

        sql = f"UPDATE products SET name='{name}', category='{category}', quantity={quantity}, price={price} WHERE product_id={product_id}"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("Success", "Product updated successfully!")
        root.destroy()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update product: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create main window
root = tk.Tk()
root.title("Update Product")

# Create and pack labels and entries for product ID, name, category, quantity, and price
tk.Label(root, text="Product ID:").pack()
product_id_entry = tk.Entry(root)
product_id_entry.pack()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Quantity:").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Price:").pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Create and pack update button
update_button = tk.Button(root, text="Update Product", command=update_product)
update_button.pack()

# Run the Tkinter event loop
root.mainloop()
