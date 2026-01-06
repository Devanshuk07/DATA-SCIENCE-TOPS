import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("txt change")
root.geometry("500x500")

def bg():
    root.config(bg="pink")   #root.config is used to change bg color, text color

label=tk.Label(root,text="CLICK THE BUTTON BELOW TO CHANGE COLOR", font="arial,20")
label.pack(pady=20)
button=tk.Button(root, command=bg,text="CHANGE COLOR").pack(pady=5)
root.mainloop()