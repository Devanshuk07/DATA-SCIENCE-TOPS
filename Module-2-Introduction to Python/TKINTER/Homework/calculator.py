import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("CALCULATOR")
root.geometry("500x500")

def add():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a+b
    messagebox.showinfo("RESULT",f"{c}")
def sub():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a-b
    messagebox.showinfo("RESULT",f"{c}")
def mult():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a*b
    messagebox.showinfo("RESULT",f"{c}")
def div():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a/b
    messagebox.showinfo("RESULT",f"{c}")

label1=tk.Label(root, text="ENTER NUMBER :").pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="ENTER NUMBER :").pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button1=tk.Button(root, command=add, text="+",width=4,height=1,font="arial,14")
button1.place(x=180,y=150)
button2=tk.Button(root, command=sub, text="-",width=4,height=1,font="arial,14")
button2.place(x=280,y=150)
button3=tk.Button(root, command=mult, text="*",width=4,height=1,font="arial,14")
button3.place(x=180,y=210)
button4=tk.Button(root, command=div, text="/",width=4,height=1,font="arial,14")
button4.place(x=280,y=210)
root.mainloop()