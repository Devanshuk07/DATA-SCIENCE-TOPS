import tkinter as tk
from tkinter import messagebox

def evaluate():
    try:     # code that may cause an error
        a= entry.get()     # e.g. 2+3*4
        b= eval(a)    # evaluates the expression
        messagebox.showinfo("Result", f"Result = {b}")
    except:    #code that runs if error occurs
        messagebox.showerror("Error", "Invalid Expression")

root = tk.Tk()
root.title("EVALUATE")
root.geometry("300x150")

label=tk.Label(root, text="Enter Expression:").pack(pady=5)    # you can also write this .pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=10)

button=tk.Button(root, text="Evaluate", command=evaluate)
button.pack(pady=5)

root.mainloop()