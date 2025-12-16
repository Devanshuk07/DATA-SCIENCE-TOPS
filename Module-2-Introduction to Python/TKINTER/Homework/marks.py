import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("MARKS")
root.geometry("500x500")

def mark():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    d=int(entry4.get())
    e=int(entry5.get())
    tot=a+b+c+d+e
    avg=(a+b+c+d+e)/5
    return tk.messagebox.showinfo("TOTAL AND AVG",f"TOTAL OF ALL YOUR MARKS IS :{tot}\nAVG OF ALL YOUR MARKS IS :{avg}")

label1=tk.Label(root, text="ENTER MATHS MARKS")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="ENTER SCIENCE MARKS")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

label3=tk.Label(root, text="ENTER HISTORY MARKS")
label3.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)

label4=tk.Label(root, text="ENTER GEOGRAPHY MARKS")
label4.pack(pady=5)
entry4=tk.Entry(root)
entry4.pack(pady=5)

label5=tk.Label(root, text="ENTER COMPUTER MARKS")
label5.pack(pady=5)
entry5=tk.Entry(root)
entry5.pack(pady=5)

button=tk.Button(root,command=mark,text="CLICK HERE FOR TOTAL AND AVG")
button.pack(pady=5)

root.mainloop()