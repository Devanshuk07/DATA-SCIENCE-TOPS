import tkinter as tk
import tkinter.messagebox as messagebox
def sis():
    a=str(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    return tk.messagebox.showinfo("EMPLOY REGISTERED",f"EMPLOY NAME IS :{a}\nEMPLOY ID IS :{b} \nEMPLY SALARY IS :{c}")
root=tk.Tk()
root.title("NAME ID SALARY")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER YOUR NAME :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="ENTER YOUR ID :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

label3=tk.Label(root, text="ENTER YOUR SALARY :")
label3.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)

button=tk.Button(root, command=sis,text="REGISTER")
button.pack(pady=5)

root.mainloop()