import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

#画像を白黒にしてぼかす
def dispPhoto(path):
    newImage = PIL.Image.open(path).convert("L").resize((15,15)).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

#画像選択
def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

#ボタンを押すとファイル選択することになる
btn = tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()