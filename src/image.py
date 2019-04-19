import os
import subprocess
from .path import regex_path

def copy_image(image_path):
    image_path_escape_chars = regex_path(image_path)
    # extension = os.path.splitext(image_path)[1]
    new_image_name = 'temp'
    destiny_dir = os.getcwd() + '/images/' + new_image_name
    commandline = "cp {} {}".format(image_path_escape_chars, destiny_dir)
    subprocess.call(commandline, shell=True)
