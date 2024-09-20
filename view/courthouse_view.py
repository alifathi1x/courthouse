import textwrap
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox as msg


def open_new_window():
    # Function to open the new window directly
    def open_new_window():
        # Create the new window
        new_window = tk.Tk()
        new_window.geometry("500x500")
        new_window.title("Lawyer Info")

        tk.Label(new_window, text="You signed in as lawyer", font="system 10").place(x=160, y=10)

        tk.Label(new_window, text="Name:", font="arial 12 bold").place(x=20, y=60)
        entry_name = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_name.place(x=80, y=60)

        tk.Label(new_window, text="Family:", font="arial 12 bold").place(x=15, y=120)
        entry_family = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_family.place(x=80, y=120)

        tk.Checkbutton(new_window, text="Lawyer license:", font="arial 12 bold").place(x=300, y=80)

        tk.Label(new_window, text="Lawyer Number:", font="arial 12 bold").place(x=10, y=180)
        entry_lawyer_number = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_lawyer_number.place(x=145, y=180)

        # Save function to capture input data and display in a messagebox
        def save_info():
            name = entry_name.get()
            family = entry_family.get()
            lawyer_number = entry_lawyer_number.get()

            if name and family and lawyer_number:
                msg.showinfo("Information Saved",
                             f"Name: {name}\nFamily: {family}\nLawyer Number: {lawyer_number}")
            else:
                msg.showwarning("Incomplete Data", "Please fill in all fields before saving.")

        # Save button
        save_button = tk.Button(new_window, text="Save", font="arial 12 bold", command=save_info)
        save_button.place(x=200, y=250)

        new_window.mainloop()

    open_new_window()


def open_new_window2():
    def open_new_window():
        # Create the new window
        new_window = tk.Tk()
        new_window.geometry("500x500")
        new_window.title("Lawyer Info")

        tk.Label(new_window, text="You signed in as lawyer", font="system 10").place(x=160, y=10)

        tk.Label(new_window, text="Name:", font="arial 12 bold").place(x=20, y=60)
        entry_name = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_name.place(x=80, y=60)

        tk.Label(new_window, text="Family:", font="arial 12 bold").place(x=15, y=120)
        entry_family = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_family.place(x=80, y=120)

        tk.Label(new_window, text="national ID:", font="arial 12 bold").place(x=10, y=180)
        entry_national_id = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_national_id.place(x=110, y=180)

        tk.Label(new_window, text="Address:", font="arial 12 bold").place(x=10, y=245)
        entry_address = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_address.place(x=100, y=245)

        tk.Label(new_window, text="Crime-type:", font="arial 12 bold").place(x=10, y=305)
        entry_crime_type = tk.Entry(new_window, font="arial 10 bold", bd=3)
        entry_crime_type.place(x=110, y=305)

        tk.Label(new_window, text="Crime Report:", font="arial 12 bold").place(x=10, y=350)
        entry_crime_report = tk.Text(new_window, font="arial 10 bold", bd=3, width=40, height=5)
        entry_crime_report.place(x=10, y=390)

        # Save function to capture input data and display in a messagebox
        def save_info():
            name = entry_name.get()
            family = entry_family.get()
            national_id = entry_national_id.get()
            address = entry_address.get()
            crime_type = entry_crime_type.get()

            if name and family and national_id and address and crime_type:
                msg.showinfo("Information Saved",
                             f"Name: {name}\n Family: {family}\n national_id: {national_id} address: {address}\n crime_type: {crime_type}\n")
            else:
                msg.showwarning("Incomplete Data", "Please fill in all fields before saving.")

        # Save button
        save_button = tk.Button(new_window, text="Save", font="arial 12 bold", command=save_info)
        save_button.place(x=400, y=450)

        new_window.mainloop()

    open_new_window()


root = tk.Tk()
root.title("Court House")
root.geometry("600x600")
img = Image.open(r"C:\Users\Ali\PycharmProjects\courthouse\view\resourse\a.png")
img = img.resize((600, 630))
img = ImageTk.PhotoImage(img)
tk.Label(master=root, image=img).pack(fill=tk.BOTH, expand=True)
tk.Label(root, text="you sign is as:", font="system 15").place(x=240, y=60)
tk.Label(root, text="Welcome!!", font="arial 20 bold").place(x=230, y=20)
tk.Button(root, text="lawyer", command=open_new_window, font="arial 17 bold").place(x=140, y=100)
tk.Button(root, text="criminal person", command=open_new_window2, font="arial 17 bold").place(x=340, y=100)
root.mainloop()
