import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("GROSS SALARY")
root.geometry("500x500")

def gross():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    g=a+b+c
    return messagebox.showinfo("GROSS SALARY :",f"GROSS SALARY IS :{g}")

label1=tk.Label(root,text="ENTER YOUR BASIC SALARY")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root,text="ENTER YOUR ALLOWANCE")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

label3=tk.Label(root,text="ENTER YOUR BONUS")
label3.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)

button=tk.Button(root, command=gross,text="GROSS SALARY")
button.pack(pady=5)

root.mainloop()
