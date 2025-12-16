import tkinter as tk
from tkinter import messagebox

def reverse():
    try:
        a = entry.get()  # get input as string
        b = a[::-1]  # reverse string----[start:stop:step]
        messagebox.showinfo("Reversed Number", f"Reversed: {b}")
    except:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Reverse Number")
root.geometry("500x500")

tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Reverse", command=reverse).pack(pady=10)

root.mainloop()