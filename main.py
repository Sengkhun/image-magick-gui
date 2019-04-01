import tkinter as tk
import subprocess

def grey_scale():
  subprocess.run(["ls", "-l"])

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

button = tk.Button(canvas, text="Grey Scale", command=grey_scale)
button.pack()

img = tk.PhotoImage(file='picture.png')
label = tk.Label(canvas, image=img)
label.pack()

root.mainloop()