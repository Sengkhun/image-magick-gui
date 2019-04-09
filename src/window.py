import os
import tkinter as tk

#==============================================

WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 600

#==============================================

def center_window(window):
    window.update()

    # Gets the requested values of the height and widht.
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    windowWidth = windowWidth if windowWidth > WINDOW_MIN_WIDTH else WINDOW_MIN_WIDTH
    windowHeight = windowHeight if windowHeight > WINDOW_MIN_HEIGHT else WINDOW_MIN_HEIGHT

    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int((window.winfo_screenheight() - 75)/2 - windowHeight/2)

    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))

#==============================================

def create_window():
    window = tk.Tk()
    window.title('Image Magick GUI')
    window.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
    window.filename = '{}/picture.png'.format(os.getcwd())
    return window
