import tkinter as tk

root=tk.Tk()
root.title("CLEAR INPUT")
root.geometry("500x500")

def clar():
    a=entry1.get()
    b=entry2.get()
    entry1.delete(0, tk.END)   #entry1.delete(0, tk.END) is used to Delete all text from the input field named entry1
    entry2.delete(0, tk.END)   # 0--is for starting index means first character
                                # tk.END is used for ending index means last character. 
label1=tk.Label(root, text="NAME :").pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)

label2=tk.Label(root, text="EMAIL :").pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

button=tk.Button(root, command=clar, text="CLEAR ALL").pack(pady=20)
root.mainloop()