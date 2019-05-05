import os
import tkinter as tk
import subprocess

from PIL import Image
from PIL import ImageTk

from src.window import create_window, center_window
from src.menu import create_menu
# from src.toolbar import create_toolbar
from src.image import convert_to_icon, manage_main_image

#==============================================

INNER_PADDING = 4
PAD_X = 4
PAD_Y = 2
BLACK = "#535353"
WHITE = "#dddddd"
SIZE = 15
MAX_IMG_SIZE = 400

#==============================================

def grey_scale(window, panel):
    # convert picture.png -colorspace LinearGray out.png
    commandline = "convert {} -colorspace LinearGray {}".format(window.filename, window.filename)
    subprocess.call(commandline, shell=True)
    img = manage_main_image(window)
    panel.configure(image=img)
    panel.image = img
    print('Grayscaled!')

def rotate(window, panel):
    # convert picture.png -colorspace LinearGray out.png
    commandline = "convert -rotate -90 {} {}".format(window.filename, window.filename)
    subprocess.call(commandline, shell=True)
    img = manage_main_image(window)
    panel.configure(image=img)
    panel.image = img
    print('Rotated!')

#==============================================

def main():
    # inital window
    window = create_window()
    window.filename = os.getcwd() + '/temp/image'  # default image
    
    main_img_canvas = manage_main_image(window)
    
    canvas = tk.Frame(window)
    panel = tk.Label(canvas, image=main_img_canvas)
    toolbar = tk.Frame(window, bg=BLACK)

    # menu
    create_menu(window, panel)

    # toolbar
    grey_icon = convert_to_icon("icons/grey.png", SIZE)
    grey_btn = tk.Button(toolbar, image=grey_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING, command=lambda:grey_scale(window, panel))
    grey_btn.grid(column=0, row=0, sticky='nesw', padx=PAD_X, pady=PAD_Y)

    rotate_icon = convert_to_icon("icons/rotate.png", SIZE)
    rotate_btn = tk.Button(toolbar, image=rotate_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING, command=lambda:rotate(window, panel))
    rotate_btn.grid(column=0, row=1, sticky='nesw', padx=PAD_X, pady=PAD_Y)

    resize_icon = convert_to_icon("icons/resize.png", SIZE)
    resize_btn = tk.Button(toolbar, image=resize_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING)
    resize_btn.grid(column=0, row=2, sticky='nesw', padx=PAD_X, pady=PAD_Y)

    crop_icon = convert_to_icon("icons/crop.png", SIZE)
    crop_btn = tk.Button(toolbar, image=crop_icon, width=SIZE, height=SIZE, padx=INNER_PADDING, pady=INNER_PADDING)
    crop_btn.grid(column=0, row=3, sticky='nesw', padx=PAD_X, pady=PAD_Y)
    
    # pack
    toolbar.pack(side=tk.LEFT, fill=tk.Y)
    canvas.pack()
    panel.pack()

    center_window(window)
    window.mainloop()

if __name__ == '__main__':
    main()