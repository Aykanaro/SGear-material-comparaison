# -*- coding: utf-8 -*-
"""
@author: Aykanaro
"""

from tkinter import *

def display():
    print('5')

root = Tk()

run = Button(root, text='run', command=display)
run.pack()

root.mainloop()