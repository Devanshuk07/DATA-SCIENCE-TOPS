import tkinter as tk
import tkinter.messagebox as messagebox
import datetime

root=tk.Tk()
root.title("CURRENT DATE AND TIME")
root.geometry("500x500")
def cur():
    a=datetime.datetime.now()
    messagebox.showinfo("CURRENT",f"{a}")

label=tk.Label(root)
label.pack(pady=5)

button=tk.Button(root,command=cur,text="CLICK ME").pack(pady=5)

root.mainloop()