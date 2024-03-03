import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    # For demonstration, hardcoding username and password
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Page")

#background
img = Image.open(r"C:\Users\Smriti Khanal\Pictures\shopping-bag-cart_23-2148879372.png")
photo = ImageTk.PhotoImage(img)
w = photo.width()
h = photo.height()

# make the root window the size of the image
root.geometry("%dx%d" % (w, h))

background_label = Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#top label
groceries_label = tk.Label(root, text="GROCERIES GALORE", font=("Akronim", 36))
groceries_label.place(relx=0.3, rely=0.2, anchor=CENTER)

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.place(relx=0.2, rely=0.3, anchor=E)

username_entry = tk.Entry(root)
username_entry.place(relx=0.25, rely=0.3, anchor=CENTER)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.place(relx=0.2, rely=0.35, anchor=E)

password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.25, rely=0.35, anchor=CENTER)

# Login button
login_button = tk.Button(root, text="Login", command=authenticate)
login_button.place(relx=0.25, rely=0.4, anchor=CENTER)

#signup
signup_label=tk.Label(root,text="Don't have an account ? Sign up here!")
signup_label.place(relx=0.28, rely=0.45, anchor=E)

def callback():
 execfile('Register.py')
signup_button = tk.Button(root, text="signup", command=callback)
signup_button.place(relx=0.3, rely=0.45, anchor=CENTER)



root.mainloop()