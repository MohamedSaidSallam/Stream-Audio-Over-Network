import tkinter as tk
from tkinter import ttk

from StreamAudioOverNetwork.audioutility import (getDeviceInfoString,
                                                 getValidDevicesList)
from StreamAudioOverNetwork.network.networkutility import getLocalIP
from StreamAudioOverNetwork.view.utility import setGrid

isStreaming = True

RECEIVE_TAB_INDEX = 1


def getSendTab(notebook):
    sendTab = ttk.Frame(notebook)

    header = tk.Label(sendTab, text="Available Device(s)")
    setGrid(header)

    devicesList = tk.Listbox(sendTab)
    setGrid(devicesList, row=1)

    validDevices = getValidDevicesList()

    for _, name in validDevices:
        devicesList.insert(0, name)

    validDevices.reverse()

    portLabel = tk.Label(sendTab, text="Port: ")
    portTextBox = tk.Entry(sendTab)
    portTextBox.insert(0, '5000')

    setGrid(portLabel, row=2, colSpan=1)
    setGrid(portTextBox, col=1, row=2, colSpan=1)

    def getInfoText(selectionIndex):
        return getDeviceInfoString(validDevices[selectionIndex][0]) + f'\n Local IP: {getLocalIP()}'

    def callback(event):
        selectionIndex = event.widget.curselection()
        if len(selectionIndex) == 0:
            return
        else:
            selectionIndex = selectionIndex[0]
        someInfo.configure(text=getInfoText(selectionIndex))

    devicesList.bind("<<ListboxSelect>>", callback)

    devicesList.select_set(0)
    someInfo = tk.Label(sendTab, text=getInfoText(0))

    setGrid(someInfo, row=3)

    def onStreamClick():
        global isStreaming
        if isStreaming:
            isStreaming = False

            port = int(portTextBox.get())
            selectedDeviceIndex = devicesList.curselection()[0]

            notebook.tab(RECEIVE_TAB_INDEX, state="disabled")
            toggleStreamingButton.configure(text="Stop Streaming")
        else:
            isStreaming = True

            notebook.tab(RECEIVE_TAB_INDEX, state="normal")
            toggleStreamingButton.configure(text="Start Streaming")

    toggleStreamingButton = tk.Button(sendTab,
                                      text="Start Streaming",
                                      command=onStreamClick,
                                      )
    setGrid(toggleStreamingButton, row=4)

    return sendTab
