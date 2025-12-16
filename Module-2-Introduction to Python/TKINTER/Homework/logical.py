import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("LOGICAL OPERATOR")
root.geometry("500x500")

def rel():
    a=20
    b=30
    if not a>=50 and b>=20:
        #a>=20 or b=="dev":    # OR means any 1 condition must be true
        #a>=20 and b=="dev"
        label1.config(text="NUMBER A ")   #.config(text="")--used to print any conditional statement
    else:
        label1.config(text="NUMBER B")

label1=tk.Label(root,text="")
label1.pack(pady=5)
# entry1=tk.Entry(root)
# entry1.pack(pady=5)

button=tk.Button(root, command=rel,text="CLICK ME")
button.pack(pady=5)

root.mainloop()