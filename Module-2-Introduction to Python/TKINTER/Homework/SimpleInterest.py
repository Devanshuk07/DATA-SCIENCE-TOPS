import tkinter as tk
import tkinter.messagebox as messagebox
def si():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    sim=(a*b*c)/100
    return tk.messagebox.showinfo("SI",f"SIMPLE INTEREST IS :{sim}")
root=tk.Tk()
root.title("SI")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER PRINCILE FOR SI :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="ENTER TIME FOR SI :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

label3=tk.Label(root, text="ENTER RATE FOR SI :")
label3.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)

button=tk.Button(root, command=si,text="SIMPLE INTEREST")
button.pack(pady=5)

root.mainloop()
