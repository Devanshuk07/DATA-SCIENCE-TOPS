import tkinter as tk
import tkinter.messagebox as messagebox

def stor():
    a=str(entry1.get())
    b=str(entry2.get())
    messagebox.showinfo("SAVED SUCCESSFULLY",f"MY NAME IS :{a}\nMY EMAIL IS :{b}")

root=tk.Tk()
root.title("Name email")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER YOUR NAME :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)
label2=tk.Label(root, text="ENTER YOUR EMAIL :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=stor,text="CLICK TO SUBMIT")
button.pack(pady=5)

root.mainloop()
