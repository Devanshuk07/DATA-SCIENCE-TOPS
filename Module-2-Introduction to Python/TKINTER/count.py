import tkinter as tk

count=0
root=tk.Tk()
root.title("CLICK COUNT")
root.geometry("800x800")

def count1():
    label.config(text=str(count))
def count2():
    global count
    count+=1
    count1()
def count3():
    global count
    count-=1
    count1()
def count4():
    global count
    count=0
    count1()


label=tk.Label(root, text="0",font=("ariel",50))
label.pack(pady=50)

button=tk.Button(root, command=count2, text="+",font=("ariel",20))
button.pack(pady=50)
button=tk.Button(root, command=count3, text="-",font=("ariel",20))
button.pack(pady=50)
button=tk.Button(root, command=count4, text="RESET",font=("ariel",20))
button.pack(pady=50)

root.mainloop()