import tkinter as tk
import subprocess

from src.window import create_window, center_window
from src.menu import create_menu

#==============================================

def grey_scale(window, img):
  # convert picture.png -colorspace LinearGray out.png
  commandline = "convert {} -colorspace LinearGray {}".format(window.filename, window.filename)
  subprocess.call(commandline, shell=True)
  img.configure(file=window.filename)

def main():
  # inital window
  window = create_window()
  create_menu(window)

  canvas = tk.Canvas(window)
  img = tk.PhotoImage(file=window.filename)
  
  label = tk.Label(canvas, image=img)
  button = tk.Button(canvas, text="Grey Scale", command=lambda:grey_scale(window, img))

  canvas.pack()
  button.pack()
  label.pack()

  center_window(window)
  window.mainloop()

if __name__ == '__main__':
  main()