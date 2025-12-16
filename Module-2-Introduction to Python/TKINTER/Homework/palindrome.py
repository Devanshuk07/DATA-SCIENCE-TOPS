import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("PALINDROME")
root.geometry("500x500")

def pal():
        a = str(entry.get())  # get input as string
        b = a[::-1]  # reverse string----[start:stop:step]
        if a==b:
            messagebox.showinfo("result",f"THIS IS PALINDROME")
        else:
            messagebox.showinfo("result",f"NOT A PALINDROME")
 
label=tk.Label(root, text="ENTER NAME TO SEE IS IT PALINDROME :").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="CHECK", command=pal).pack(pady=10)

root.mainloop()