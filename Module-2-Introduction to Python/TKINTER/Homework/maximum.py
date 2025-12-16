import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("MAXIMUM")
root.geometry("500x500")

def max():
    a=int(entry1.get())
    b=int(entry2.get())
    if a>b:
        messagebox.showinfo("result",f"A IS GREATER :{a}")
    elif b>a:
        messagebox.showinfo("result",f"B IS GREATER :{b}")
    elif a==b:
        messagebox.showinfo("result","A AND B IS EQUAL")

label1=tk.Label(root, text="ENTER VALUE OF A").pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)
label2=tk.Label(root, text="ENTER VALUE OF B").pack(pady=5)
entry2=tk.Entry(root)#.pack(pady=5) we cannot put it at entry as it will return none value so error will occur
entry2.pack(pady=5)

button=tk.Button(root, command=max,text="CLICK TO GET GREATER VALUE").pack(pady=5)
root.mainloop()