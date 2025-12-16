import tkinter as tk

root=tk.Tk()
root.title("ARITHMETIC OPERATION")
root.geometry("500x500")

def art():
    a=int(entry.get())
    if a % 2==0:
        label.config(text="NUMBER IS EVEN")
    else:
        label.config(text="NUMBER IS ODD")

label=tk.Label(root,text="ENTER NUMBER OF YOUR CHOICE")
label.pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root,command=art,text="ODD/EVEN")
button.pack(pady=5)

root.mainloop()