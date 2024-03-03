import mysql.connector
import tkinter as tk
from tkinter import messagebox

def update_employee_info():
    employee_id = aeid_entry.get()
    value2 = apassword_entry.get()
    value3 = a_phno_entry.get()
    value4 = a_email_entry.get()  # New line to get email value

    database = "grocery_store"
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="sagarme",
        database=database
    )

    cursor = db.cursor()
    cursor.execute("UPDATE employees SET password=%s WHERE employee_id=%s", (value2, employee_id))
    cursor.execute("UPDATE employees SET phone=%s WHERE employee_id=%s", (value3, employee_id))
    cursor.execute("UPDATE employees SET email=%s WHERE employee_id=%s", (value4, employee_id))  # New line to update email
    db.commit()

    messagebox.showinfo("Success", "Employee information updated successfully")
    aeid_entry.delete(0, 'end')
    apassword_entry.delete(0, 'end')
    a_phno_entry.delete(0, 'end')
    a_email_entry.delete(0, 'end')  # New line to clear email entry field

# Create a tkinter window
window = tk.Tk()
window.title("Update Employee Information")

# Create input fields and labels
aeid_label = tk.Label(window, text="Employee ID:")
aeid_label.pack()
aeid_entry = tk.Entry(window)
aeid_entry.pack()

apassword_label = tk.Label(window, text="New Password:")
apassword_label.pack()
apassword_entry = tk.Entry(window, show="*")
apassword_entry.pack()

a_phno_label = tk.Label(window, text="New Phone Number:")
a_phno_label.pack()
a_phno_entry = tk.Entry(window)
a_phno_entry.pack()

a_email_label = tk.Label(window, text="New Email:")  # New line to create email label
a_email_label.pack()  # New line to pack email label
a_email_entry = tk.Entry(window)  # New line to create email entry field
a_email_entry.pack()  # New line to pack email entry field

update_button = tk.Button(window, text="Update Info", command=update_employee_info)
update_button.pack()

window.mainloop()
