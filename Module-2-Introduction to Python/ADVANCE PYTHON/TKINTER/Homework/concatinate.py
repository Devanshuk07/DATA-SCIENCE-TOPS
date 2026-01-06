import tkinter as tk
import tkinter.messagebox as messagebox

def stor():
    a=entry1.get()
    b=entry2.get()
    c=a+b
    return tk.messagebox.showinfo("CONCATINATE :",f"CONCATINATED STRING IS :{c}")
root=tk.Tk()
root.title("CONCATINATE")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER ANY STRING :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)
label2=tk.Label(root, text="ENTER ANY STRING :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=stor,text="CONCATINATE")
button.pack(pady=5)

root.mainloop()
