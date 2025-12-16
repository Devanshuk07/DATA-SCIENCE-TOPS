import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("Swapping")
root.geometry("500x500")

def swap1():
    a=int(entry1.get())  # 20
    b=int(entry2.get())  #30
    c=a
    a=b
    b=c
    return tk.messagebox.showinfo("YOUR SWAP VALUE IS",f"After swapping: \n Value a = {a} \n Value b = {b}")
    #f is used to tell python that i want to put actual value of a and b inside this string.
    #{} brackets is used to insert the value of a variable.
label1=tk.Label(root, text="ENTER VALUE OF A")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root,text="ENTER VALUE OF B")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=swap1, text="AFTER SWAPPING VALUE IS")
button.pack(pady=5)

root.mainloop()

    