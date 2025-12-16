import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("txt change")
root.geometry("500x500")

def txt():
    label.config(text="TEXT CHANGED")   #when button is clicked function is called and text changed will be print
    #config error means --label should be given pack differntly not within 1 line.as pack()--none.
label=tk.Label(root,text="ORIGINAL TEXT",font="ariel,20")
label.pack(pady=20)
button=tk.Button(root, command=txt,text="CLICK ME").pack(pady=5)
root.mainloop()