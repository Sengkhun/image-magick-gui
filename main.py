import os
import tkinter as tk
import subprocess

from PIL import Image
from PIL import ImageTk

from src.window import create_window, center_window
from src.menu import create_menu
# from src.toolbar import create_toolbar
from src.image import convert_to_icon

#==============================================

INNER_PADDING = 4
PAD_X = 4
PAD_Y = 2
BLACK = "#535353"
WHITE = "#dddddd"
SIZE = 15

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

    toolbar = tk.Frame(window, bg=BLACK)

    grey_icon = convert_to_icon("icons/grey.png", SIZE)
    grey_btn = tk.Button(toolbar, image=grey_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING)
    grey_btn.grid(column=0, row=0, sticky='nesw', padx=PAD_X, pady=PAD_Y)

    rotate_icon = convert_to_icon("icons/rotate.png", SIZE)
    rotate_btn = tk.Button(toolbar, image=rotate_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING)
    rotate_btn.grid(column=0, row=1, sticky='nesw', padx=PAD_X, pady=PAD_Y)

    resize_icon = convert_to_icon("icons/resize.png", SIZE)
    resize_btn = tk.Button(toolbar, image=resize_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING)
    resize_btn.grid(column=0, row=2, sticky='nesw', padx=PAD_X, pady=PAD_Y)

    crop_icon = convert_to_icon("icons/crop.png", SIZE)
    crop_btn = tk.Button(toolbar, image=crop_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING)
    crop_btn.grid(column=0, row=3, sticky='nesw', padx=PAD_X, pady=PAD_Y)
    toolbar.pack(side=tk.LEFT, fill=tk.Y)
    
    label = tk.Label(canvas, image=img, height=400, width=400)

    canvas.pack()
    label.pack()

    center_window(window)

    window.mainloop()

if __name__ == '__main__':
    main()