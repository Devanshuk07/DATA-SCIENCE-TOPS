import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("RELATIONAL OPERATOR")
root.geometry("500x500")

def rel():
    a=10
    b=5
    if a>b:
        label1.config(text="NUMBER A IS GREATER")   #.config(text="")--used to print any conditional statement
    else:
        label1.config(text="NUMBER A IS LESS THAN B")

label1=tk.Label(root,text="")
label1.pack(pady=5)
# entry1=tk.Entry(root)
# entry1.pack(pady=5)

button=tk.Button(root, command=rel,text="CLICK ME")
button.pack(pady=5)

root.mainloop()