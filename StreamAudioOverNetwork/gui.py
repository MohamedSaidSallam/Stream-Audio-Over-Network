import tkinter as tk
from tkinter import ttk

from StreamAudioOverNetwork.view.receivetab import getReceiveTab
from StreamAudioOverNetwork.view.sendtab import getSendTab

window = tk.Tk()

window.title("Stream Audio Over Network")

notebook = ttk.Notebook(window)


notebook.add(getSendTab(notebook), text='Send Audio')
notebook.add(getReceiveTab(notebook), text='Receive Audio')
notebook.pack(expand=1, fill="both")


def main():
    window.mainloop()
