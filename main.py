import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def grey_scale():
  # convert picture.png -colorspace LinearGray out.png
  commandline = "convert {} -colorspace LinearGray {}".format(window.filename, window.filename)
  subprocess.call(commandline, shell=True)
  img.configure(file=window.filename)

def donothing(name='button'):
  print('click', name)

def file_open_menu():
  window.filename = filedialog.askopenfilename(title = "Select image", filetypes = (("Image files","*.jpg *.jpeg *.png"), ("All files","*.*")))
  img.configure(file=window.filename)

# inital window
window = tk.Tk()
window.title('Image Magick GUI')
window.filename = '{}/picture.png'.format(os.getcwd())

# menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open...", command=file_open_menu)
filemenu.add_command(label="Save", command=donothing)
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
# end of menu

canvas = tk.Canvas(window)
canvas.pack()

button = tk.Button(canvas, text="Grey Scale", command=grey_scale)
button.pack()

img = tk.PhotoImage(file=window.filename)
label = tk.Label(canvas, image=img)
label.pack()

window.mainloop()