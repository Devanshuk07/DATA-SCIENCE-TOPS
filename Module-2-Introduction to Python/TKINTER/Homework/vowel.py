import tkinter as tk
import tkinter.messagebox as messagebox

root=tk.Tk()
root.title("MEMBERSHIP")
root.geometry("500x500")

vowel=['a','e','i','o','u']

def check_vowel():
    vow=str(entry.get()).lower()    #.lower()--differences in uppercase/lowercase don’t matter.

    if vow in vowel:
        messagebox.showinfo("RESULT","VOWEL")
    else:
        messagebox.showinfo("RESULT","NOT A VOWEL")

label=tk.Label(root,text="ENTER ANY ALPHABET")
label.pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root,command=check_vowel,text="CLICK TO CHECK")
button.pack(pady=5)

root.mainloop()