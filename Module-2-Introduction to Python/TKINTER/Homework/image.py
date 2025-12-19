import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("image example")

image=Image.open("dhurandhar-ranveer-singh-aditya-dhar-x-reviews-dhurandhar-x-reviews.webp")
photo=ImageTk.PhotoImage(image)

label=tk.Label(root,image=photo)
label.pack(pady=5)

root.mainloop()