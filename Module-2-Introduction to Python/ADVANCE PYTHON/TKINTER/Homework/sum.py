import tkinter as tk
import tkinter.messagebox as messagebox
root=tk.Tk()
root.title("SUM OF TWO NUMBERS")
root.geometry("500x500")
def sum():
    a=float(entry1.get())
    b=float(entry2.get())
    result=a+b
    return tk.messagebox.showinfo("SUM IS",result)

label1=tk.Label(root, text="PLEASE ENTER VALUE OF A :")
label1.pack(pady=30)
entry1=tk.Entry(root)
entry1.pack(pady=30)

label2=tk.Label(root, text="PLEASE ENTER VALUE OF B :")
label2.pack(pady=30)
entry2=tk.Entry(root)
entry2.pack(pady=30)

button=tk.Button(root, command=sum,text="SUM")
button.pack(pady=30)

root.mainloop()