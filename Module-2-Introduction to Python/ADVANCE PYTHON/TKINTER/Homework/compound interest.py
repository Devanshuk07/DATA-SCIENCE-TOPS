import tkinter as tk
import tkinter.messagebox as messagebox
def ci():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    com=a*(1+b/100)**c
    return tk.messagebox.showinfo("CI",f"COMPOUND INTEREST IS :{com}")
root=tk.Tk()
root.title("SI")
root.geometry("500x500")

label1=tk.Label(root, text="ENTER PRINCILE FOR CI :")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="ENTER TIME FOR CI :")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

label3=tk.Label(root, text="ENTER RATE FOR CI :")
label3.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)

button=tk.Button(root, command=ci,text="COMPOUND INTEREST")
button.pack(pady=5)

root.mainloop()
