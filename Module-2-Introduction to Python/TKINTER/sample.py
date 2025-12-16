import tkinter as tk
#To create the main application windows
root = tk.Tk() # tk.Tk (T=capital)
#to store 
root.title("TKINTER WINDOW")
#this is for giving title
root.geometry("1000x500")
#create the frame size 1000=x and 500=y
label = tk.Label(root,text="HELLO KD ❤️", font=("arial",30))
#label = tk.label used to give text
label.pack(pady=20)
#label.pack is used to set position from top to bottom 1st-title 2nd-geometry 3rd-text like this
#pady means =space
root.mainloop()
#this is used to print windows in GUI like print