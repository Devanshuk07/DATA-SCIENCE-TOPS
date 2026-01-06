import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("DIV BY 5 AND 11")
root.geometry("500x500")
def div():
    a=int(entry.get())
    if a%4==0:
        label.config(text="LEAP YEAR")
    else:
        label.config(text="NOT A LEAP YEAR")

label=tk.Label(root, text="ENTER THE YEAR")
label.pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root, command=div, text="CLICK TO CHECK LEAP YEAR")
button.pack(pady=5)

root.mainloop()
