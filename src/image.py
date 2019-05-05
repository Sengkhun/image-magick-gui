import os
import subprocess
from PIL import Image
from PIL import ImageTk

from .path import regex_path

#==============================================

WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 600

#==============================================

def copy_image(image_path):
    image_path_escape_chars = regex_path(image_path)
    new_image_name = 'image'
    destiny_dir = os.getcwd() + '/temp/' + new_image_name
    commandline = "cp {} {}".format(image_path_escape_chars, destiny_dir)
    subprocess.call(commandline, shell=True)
    print('Copied!')
    return destiny_dir

#==============================================

def save_img():
    f = open("temp/path.txt", "r")
    destiny_path = f.read()
    
    is_exist = os.path.exists(destiny_path)
    if is_exist:
        destiny_path_escape_chars = regex_path(destiny_path)
        new_image_name = 'image'
        source_dir = os.getcwd() + '/temp/' + new_image_name
        commandline = "cp {} {}".format(source_dir, destiny_path_escape_chars)
        subprocess.call(commandline, shell=True)
        print('Saved!')
    else:
        print('Image not found')

#==============================================

def convert_to_icon(image_path, size):
    img = Image.open(image_path)
    img = img.resize((size, size), Image.ANTIALIAS)
    icon =  ImageTk.PhotoImage(img)
    return icon

#==============================================

def manage_main_image(window):
    is_exist = os.path.exists(window.filename)
    if is_exist:
        main_img = Image.open(window.filename)
        img_width, img_height = main_img.size

        width = img_width if img_width < WINDOW_MIN_WIDTH else WINDOW_MIN_WIDTH
        height = img_height if img_height < WINDOW_MIN_HEIGHT else WINDOW_MIN_HEIGHT

        if img_width < img_height:
            ratio_width = int(img_width * (height / img_height))
            main_img = main_img.resize((ratio_width, height), Image.ANTIALIAS)
            return ImageTk.PhotoImage(main_img)
        else:
            ratio_height = int(img_height * (width / img_width))
            main_img = main_img.resize((width, ratio_height), Image.ANTIALIAS)
            return ImageTk.PhotoImage(main_img)
    else:
        return ""
