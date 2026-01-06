import tkinter as tk
import tkinter.messagebox as messagebox
pi=3.14
def stor():
    a=int(entry1.get())
    b=a**2
    c=a**3
    return tk.messagebox.showinfo("SQUARE AND CUBE",f"SQUARE OF A NUMBER IS :{b}\n CUBE OF THE NUMBER IS :{c}")
root=tk.Tk()
root.title("square cube")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER THE NUMBER :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

button=tk.Button(root, command=stor,text="CLICK TO SUBMIT")
button.pack(pady=5)

root.mainloop()