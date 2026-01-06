import tkinter as tk
import tkinter.messagebox as messagebox
root=tk.Tk()
root.title("ALERT BOX")
root.geometry("400x400")
label=tk.Label(root, text="THIS IS EXAMPLE OF ALERT", font=("Ariel", 20))
label.pack(pady=40)
def user_alert():
    # print("YOU ARE ALERTED")
    return tk.messagebox.showinfo("alert", "YOU ARE ALERTED")
    #ALERT IS FOR ALERT MESSAGE LIKE POP-UP THEN GIVE YOUR MESSAGE IN ""
button=tk.Button(root, text="ALERT ME", command=user_alert, font=("Ariel", 20))
button.pack(pady=40)
#create a function to show alert box and also this must be before button
root.mainloop()