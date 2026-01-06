import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("GRADE")
root.geometry("500x500")

def grd():
    a=int(entry.get())
    if 100>=a>=85:
        messagebox.showinfo("GRADE",f"A GRADE")
    elif 84>=a>=70:
        messagebox.showinfo("GRADE",f"B GRADE")
    elif 69>=a>=50:
        messagebox.showinfo("GRADE",f"C GRADE")
    elif 49>=a>=35:
        messagebox.showinfo("GRADE",f"D GRADE")
    elif a<35:
        messagebox.showinfo("GRADE",f"YOU FAILED")
    elif a>100:
        messagebox.showinfo("GRADE",f"ERROR CHECK MARKS !!!")


label=tk.Label(root,text="ENTER YOUR MARKS").pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root, command=grd,text="CHECK GRADE").pack(pady=5)
root.mainloop()
