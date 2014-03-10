#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")

f = Figure(figsize=(5,4), dpi=100)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def _plot_sin():
	a = f.add_subplot(111)
	t = arange(0.0,3.0,0.01)
	s = sin(2*pi*t)
	a.plot(t,s)
	canvas.show()

button1 = Tk.Button(master=root, text='Plot!', command=_plot_sin)
button1.pack(side=Tk.TOP)
button2 = Tk.Button(master=root, text='Quit', command=_quit)
button2.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.