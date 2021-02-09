from tkinter.constants import NSEW


def setGrid(widget, col=0, row=0, colSpan=2):
    return widget.grid(column=col, row=row, sticky=NSEW, columnspan=colSpan)