#!/usr/bin/env python
# -*- noplot -*-
"""
A pure OO (look Ma, no pylab!) example using the tkagg backend
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
from matplotlib.figure import Figure
from Tkinter import *

root = Tk()

fig = Figure()
canvas = FigureCanvas(fig, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
ax = fig.add_subplot(111)
ax.plot([1,2,3])
ax.set_title('hi mom')
ax.grid(True)
ax.set_xlabel('time')
ax.set_ylabel('volts')
canvas.show()

root.mainloop()