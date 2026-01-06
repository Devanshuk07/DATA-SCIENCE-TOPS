import tkinter as tk
import tkinter.messagebox as messagebox
def add():
    a=float(entry1.get())   # or a=10 take input from --user=entry1.get()
    b=float(entry2.get())   # or b=20
    result=a+b
    return tk.messagebox.showinfo("THE ADDITION IS", result)
root=tk.Tk()
root.title("ADDITION")
root.geometry("500x500")
label1=tk.Label(root, text="ENTER NUMBER 1 :")
label1.pack(pady=20)
entry1=tk.Entry(root)
entry1.pack(pady=10)
#4 lines you have to write to take input from user

label2=tk.Label(root, text="ENTER NUMBER 2 :")
label2.pack(pady=20)
entry2=tk.Entry(root)
entry2.pack(pady=10)
button=tk.Button(root, command=add, text="CLICK FOR ADDITION")
button.pack(pady=20)
root.mainloop()