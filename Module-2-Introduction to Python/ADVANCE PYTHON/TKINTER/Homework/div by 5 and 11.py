import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("DIV BY 5 AND 11")
root.geometry("500x500")
def div():
    a=int(entry.get())
    if a%5==0 and a%11==0:
        label.config(text="NUMBER IS DIVISIBLE BY 5 AND 11 BOTH")
    else:
        label.config(text="NUMBER IS NOT DIVISIBLE BY 5 AND 11")

label=tk.Label(root, text="ENTER THE NUMBER OF YOUR CHOICE")
label.pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root, command=div, text="DIVISIBLE BY 5 AND 11")
button.pack(pady=5)

root.mainloop()
