import tkinter as tk
import tkinter.messagebox as messagebox
#to create the message box when click me is clicked
def kd():
    return tk.messagebox.showinfo("greeting","hello,KD")

root=tk.Tk()
root.title("button click program")
root.geometry("800x600")
button=tk.Button(root, text="click me", command=kd)

button.pack(pady=80)
root.mainloop()