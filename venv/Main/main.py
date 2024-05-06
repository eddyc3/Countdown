# The Plan for this Project is to create a app that can be used to make the Countdown Numbers Challenge.
import tkinter as tk
import math


# 101-999
'''Defined Setup to keep these elements contained in the one section'''
def setup()
    win = tk.Tk()
    win.title("Countdown Numbers Challenge")
    # Sets Window Size
    w = 600
    h = 600
    # Get Screen Width and Height
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()

    # Calculate x and y coordinates for the Tk Window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Set The Dimensions of the Screen and Where it's Placed.
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.resizable(False, False)

lnums = list(range(1, 11))
hnums = list[25, 50, 75, 100

win.mainloop()