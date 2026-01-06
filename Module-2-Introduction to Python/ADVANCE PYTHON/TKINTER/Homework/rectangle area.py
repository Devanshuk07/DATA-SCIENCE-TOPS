import tkinter as tk
import tkinter.messagebox as messagebox

def stor():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a*b
    return tk.messagebox.showinfo("AREA OF RECTANGLE IS :",f"AREA OF RECTANGLE IS :{c}")
root=tk.Tk()
root.title("rectangle")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER LENGTH OF RECTANGLE :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)
label2=tk.Label(root, text="ENTER BREATH OF RECTANGLE :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=stor,text="CLICK TO SUBMIT")
button.pack(pady=5)

root.mainloop()
