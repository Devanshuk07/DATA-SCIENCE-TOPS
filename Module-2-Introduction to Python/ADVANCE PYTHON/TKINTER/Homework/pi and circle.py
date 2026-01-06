import tkinter as tk
import tkinter.messagebox as messagebox
pi=3.14
def stor():
    a=int(entry1.get())
    c=pi*a**2
    return tk.messagebox.showinfo("CIRCLE AREA",f"AREA OF CIRCLE IS :{c}")
root=tk.Tk()
root.title("CIRCLE")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER RADIUS OF CIRCLE :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

button=tk.Button(root, command=stor,text="CLICK TO SUBMIT")
button.pack(pady=5)

root.mainloop()
