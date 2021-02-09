from tkinter.constants import NSEW


def setGrid(widget, col=0, row=0, colSpan=2):
    return widget.grid(column=col, row=row, sticky=NSEW, columnspan=colSpan)


def addRow(rowNum, *widgets):
    colSpan = 2 if len(widgets) == 1 else 1
    for i in range(len(widgets)):
        setGrid(widgets[i], i, rowNum, colSpan)
    return rowNum + 1
