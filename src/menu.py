import os
import subprocess
import tkinter as tk
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk

from .image import copy_image, save_img, manage_main_image
from .window import center_window

#==============================================

def donothing(name='button'):
    print('click', name)

#==============================================

def file_open_menu(window, panel):
    image_path = filedialog.askopenfilename(title = "Select image", filetypes = (("Image files","*.jpg *.jpeg *.png"), ("All files","*.*")))
    copy_image(image_path)

    # save original image path to file
    f = open("temp/path.txt", "w")
    f.write(image_path)
    f.close()

    img = manage_main_image(window)
    panel.configure(image=img)
    panel.image = img
    
    center_window(window)

#==============================================

def create_menu(window, panel):
    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open...", command=lambda:file_open_menu(window, panel))
    filemenu.add_command(label="Save", command=save_img)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)