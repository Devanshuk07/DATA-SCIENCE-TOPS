import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("ARITHMETIC OPERATION")
root.geometry("500x500")

def art():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    g=a%b   #module
    h=a**b  #power of
    return tk.messagebox.showinfo("ARITHMETIC OPERATION",f"ADDITION IS : {c}\nSUBSTRACTION IS : {d}\nMULTIPLICATION IS : {e}\nDIVISION IS : {f}\nMODULE IS : {g}\nPOWER IS : {h}")

label1=tk.Label(root, text="PLEASE ENTER VALUE OF A :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="PLEASE ENTER VALUE OF B :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=art,text="ARITHMETIC OPERATION")
button.pack(pady=5)

root.mainloop()