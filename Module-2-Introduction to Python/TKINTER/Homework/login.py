import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("CLEAR INPUT")
root.geometry("500x500")

def clar():
    a=entry1.get()
    b=entry2.get()
    messagebox.showinfo("WOW !","CONGRATULATIONS ! YOU ARE LOGIN")

label1=tk.Label(root, text="NAME :").pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="ROOL NO :").pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=clar, text="LOGIN").pack(pady=20)
root.mainloop()