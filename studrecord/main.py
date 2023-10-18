import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to add a student record
def add_record():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        record_list.insert('', tk.END, values=(name, age))
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both name and age.")

# Function to delete a selected record
def delete_record():
    selected_item = record_list.selection()
    if selected_item:
        record_list.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "Please select a record to delete.")

# Create the main application window
root = tk.Tk()
root.title("Student Record Management System")

# Frame for input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5)

age_label = tk.Label(input_frame, text="Age:")
age_label.grid(row=1, column=0, padx=5)
age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=1, padx=5)

# Button to add a record
add_button = tk.Button(root, text="Add Record", command=add_record)
add_button.pack(pady=5)

# Treeview for displaying records
record_list = ttk.Treeview(root, columns=('Name', 'Age'), show='headings')
record_list.heading('Name', text='Name')
record_list.heading('Age', text='Age')
record_list.pack()

# Button to delete a record
delete_button = tk.Button(root, text="Delete Record", command=delete_record)
delete_button.pack(pady=5)

# Start the application
root.mainloop()
