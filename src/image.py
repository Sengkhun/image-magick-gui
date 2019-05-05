import os
import subprocess
from PIL import Image
from PIL import ImageTk

from .path import regex_path

def copy_image(image_path):
    image_path_escape_chars = regex_path(image_path)
    # extension = os.path.splitext(image_path)[1]
    new_image_name = 'temp'
    destiny_dir = os.getcwd() + '/images/' + new_image_name
    commandline = "cp {} {}".format(image_path_escape_chars, destiny_dir)
    subprocess.call(commandline, shell=True)

def convert_to_icon(image_path, size):
    img = Image.open(image_path)
    img = img.resize((size, size), Image.ANTIALIAS)
    icon =  ImageTk.PhotoImage(img)
    return icon