import tkinter as tk
import tkinter.messagebox as messagebox
def add():
    a=float(entry1.get())
    b=float(entry2.get())
    res1=a+b
    return tk.messagebox.showinfo("the addition is :",res1)
def sub():
    a=float(entry1.get())
    b=float(entry2.get())
    res2=a-b
    return tk.messagebox.showinfo("the substraction is :",res2)
def mul():
    a=float(entry1.get())
    b=float(entry2.get())
    res3=a*b
    return tk.messagebox.showinfo("the multiplication is :",res3)
def div():
    a=float(entry1.get())
    b=float(entry2.get())
    res4=a/b
    return tk.messagebox.showinfo("the division is :",res4)

root=tk.Tk()
root.title("calculator")
root.geometry("800x800")

label1=tk.Label(root, text="ENTER NUMBER 1 :")
label1.pack(pady=50)
entry1=tk.Entry(root)
entry1.pack(pady=50)

label2=tk.Label(root, text="ENTER NUMBER 2 :")
label2.pack(pady=50)
entry2=tk.Entry(root)
entry2.pack(pady=50)

button=tk.Button(root, command=add, text="CLICK FOR ADDITION")
button.pack(pady=20)
button=tk.Button(root, command=sub, text="CLICK FOR SUBSTRACTION")
button.pack(pady=20)
button=tk.Button(root, command=mul, text="CLICK FOR MULTIPLICATION")
button.pack(pady=20)
button=tk.Button(root, command=div, text="CLICK FOR DIVISION")
button.pack(pady=20)
root.mainloop()
