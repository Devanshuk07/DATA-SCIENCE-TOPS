import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("FINDING TYPE")
root.geometry("500x500")

def check_type():
    value=entry.get()
    print(value)
    print(type(value))

label=tk.Label(root, text="ENTER ANYTHING")
label.pack(pady=30)
entry=tk.Entry(root)
entry.pack(pady=30)

button=tk.Button(root, command=check_type,text="CLICK TO GET TYPE")
button.pack(pady=30)

root.mainloop()