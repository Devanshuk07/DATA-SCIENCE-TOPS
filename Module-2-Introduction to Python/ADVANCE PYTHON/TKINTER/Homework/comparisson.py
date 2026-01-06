import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("LOGICAL OPERATOR")
root.geometry("500x500")

def rel():
    a=int(entry1.get())
    b=int(entry2.get())
    if a==b:
        #a>=20 or b=="dev":    # OR means any 1 condition must be true
        #a>=20 and b=="dev"
        messagebox.showinfo("RESULT","BOTH NUMBER IS SAME")   #messagebox.showinfo or showwarning is used with("title","message")----this is the true format
    elif a>b:                                                 #messagebox dont have text format text is used only in ---label and button
        messagebox.showinfo("RESULT","A IS GREATER")
    elif a<b:
        messagebox.showinfo("RESULT","B IS GREATER")

label1=tk.Label(root,text="ENTER VALUE OF A")
label1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root,text="ENTER VALUE OF B")
label2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)


button=tk.Button(root, command=rel,text="CLICK ME")
button.pack(pady=5)

root.mainloop()