import tkinter as tk
import random

def dispLabel():
    kuji=["daikiti","tyukiti","syokiti","kyo"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABLE")
btn = tk.Button(text="PUSH",command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()