import os
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
    window.filename = os.getcwd() + '/images/temp'  # default image

    canvas = tk.Canvas(window)
    is_exist = os.path.exists(window.filename)
    if is_exist:
        img = tk.PhotoImage(file=window.filename)
    else:
        img = tk.PhotoImage()

    create_menu(window, img)
    
    label = tk.Label(canvas, image=img)
    button = tk.Button(canvas, text="Grey Scale", command=lambda:grey_scale(window, img))

    canvas.pack()
    button.pack()
    label.pack()

    center_window(window)
    window.mainloop()

if __name__ == '__main__':
    main()