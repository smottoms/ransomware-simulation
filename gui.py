import tkinter as tk
from decryptor import *

root = tk.Tk()
root.title("Your Files Are Encrypted")
root.geometry("500x300")

label = tk.Label(root,
text="Your files have been encrypted!\nThis is a training simulation.",
fg="red",
font=("Arial",14))

label.pack(pady=20)

def decrypt():
    os.system("python decryptor.py")

btn = tk.Button(root,text="Decrypt Files",command=decrypt)
btn.pack()

root.mainloop()