import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("voting")
root.geometry("500x500")

def vot():
    a=int(entry.get())
    if a>=18:
        messagebox.showinfo("RESULT","YOU ARE ELIGIBLE FOR VOTING")
    else:
        messagebox.showinfo("RESULT","YOU ARE NOT ELIGIBLE FOR VOTING")

label=tk.Label(root,text="ENTER YOUR AGE")
label.pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root, command=vot,text="ELIGIBLY TEST")
button.pack(pady=5)

root.mainloop()