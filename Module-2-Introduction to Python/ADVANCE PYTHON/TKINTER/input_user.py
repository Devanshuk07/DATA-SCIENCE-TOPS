import tkinter as tk
import tkinter.messagebox as messagebox
def input_user():
    user_input = entry.get()
    #entry.get method to get info from user
    print("User name is :", user_input)
root = tk.Tk()
root.title("user_input")
root.geometry("400x500")
label=tk.Label(root, text="Enter your name :", font=("arial", 14))
label.pack(pady=20)
entry = tk.Entry(root, font=("arial", 14))
entry.pack(pady=20)
button=tk.Button(root, text="submit",command=input_user)
button.pack(pady=20)
root.mainloop()