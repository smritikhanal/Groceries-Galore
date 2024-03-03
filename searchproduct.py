import tkinter as tk
from tkinter import ttk
import mysql.connector

def search_product():
    value3 = name_entry.get()
    database = "grocery_store"
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="sagarme",
        database=database
    )
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM PRODUCTS WHERE name='{value3}'")
    result = cursor.fetchall()

    for row in result:
        treeview.insert('', 'end', values=row)

root = tk.Tk()
root.title("Product Search")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

name_label = ttk.Label(frame, text="Item Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = ttk.Button(frame, text="Search", command=search_product)
search_button.grid(row=0, column=2, padx=5, pady=5)

columns = ('ID', 'Category', 'Item Name', 'Cost', 'No of Items Left')
treeview = ttk.Treeview(frame, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)
treeview.grid(row=1, column=0, columnspan=3)

root.mainloop()