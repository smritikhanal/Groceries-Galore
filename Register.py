import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
 
def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
 
    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match")
    else:
        # Here you can implement your registration logic
        # For simplicity, just display the registered username
        messagebox.showinfo("Registration Successful", "Registered username: {}".format(username))
 
# Create main window
root = tk.Tk()
root.title("Registration Page")
 
# Background
img = Image.open(r"C:\Users\Smriti Khanal\Pictures\shopping-bag-cart_23-2148879372.png")
photo = ImageTk.PhotoImage(img)
w = photo.width()
h = photo.height()
 
# Make the root window the size of the image
root.geometry("%dx%d" % (w, h))
 
background_label = Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
 
# Top label
registration_label = tk.Label(root, text="REGISTER HERE", font=("Akronim", 36))
registration_label.place(relx=0.5, rely=0.1, anchor=N)
 
# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.place(relx=0.3, rely=0.3, anchor=E)
 
username_entry = tk.Entry(root)
username_entry.place(relx=0.35, rely=0.3, anchor=W)
 
# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.place(relx=0.3, rely=0.4, anchor=E)
 
password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.35, rely=0.4, anchor=W)
 
# Confirm Password label and entry
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.place(relx=0.3, rely=0.5, anchor=E)
 
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.place(relx=0.35, rely=0.5, anchor=W)
 
# Register button
register_button = tk.Button(root, text="Register", command=register)
register_button.place(relx=0.35, rely=0.6, anchor=N)
 
root.mainloop()

