import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("MEMBERSHIP")
root.geometry("500x500")

fruit=['banana','apple','watermelon','guava','pineapple','cherry','papaya']

def check_fruit():
    fru=str(entry.get()).lower()    #.lower()--differences in uppercase/lowercase don’t matter.

    if fru in fruit:
        messagebox.showinfo("RESULT","YOU ENTERED FRUIT IS IN LIST")
    else:
        messagebox.showinfo("RESULT","FRUIT YOU ENTERED IS NOT IN LIST")

label=tk.Label(root,text="ENTER THE FRUIT NAME")
label.pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root,command=check_fruit,text="CLICK TO CHECK")
button.pack(pady=5)

root.mainloop()