import tkinter as tk
from tkinter import ttk

from StreamAudioOverNetwork.audioutility import (getDeviceInfoString,
                                                 getValidDevicesList)
from StreamAudioOverNetwork.network.networkutility import getLocalIP
from StreamAudioOverNetwork.streamaudio import SendAudio
from StreamAudioOverNetwork.view.gridUtility import addRow

isStreaming = False

RECEIVE_TAB_INDEX = 1


def getSendTab(notebook):
    sendAudio = SendAudio()
    sendTab = ttk.Frame(notebook)

    rowNum = 0

    header = tk.Label(sendTab, text="Available Device(s)")
    rowNum = addRow(rowNum, header)

    devicesList = tk.Listbox(sendTab)
    rowNum = addRow(rowNum, devicesList)

    validDevices = getValidDevicesList()

    for _, name in validDevices:
        devicesList.insert(0, name)

    validDevices.reverse()

    portLabel = tk.Label(sendTab, text="Port: ")
    portTextBox = tk.Entry(sendTab)
    portTextBox.insert(0, '5000')

    rowNum = addRow(rowNum, portLabel, portTextBox)

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

    rowNum = addRow(rowNum, someInfo)

    def onStreamClick():
        global isStreaming
        if isStreaming:
            isStreaming = False

            sendAudio.stop()

            notebook.tab(RECEIVE_TAB_INDEX, state="normal")
            toggleStreamingButton.configure(text="Start Streaming")
        else:
            isStreaming = True

            port = int(portTextBox.get())
            selectedDeviceIndex = validDevices[devicesList.curselection()[
                0]][0]
            sendAudio.start(port, selectedDeviceIndex, getLocalIP())

            notebook.tab(RECEIVE_TAB_INDEX, state="disabled")
            toggleStreamingButton.configure(text="Stop Streaming")

    toggleStreamingButton = tk.Button(sendTab,
                                      text="Start Streaming",
                                      command=onStreamClick,
                                      )
    rowNum = addRow(rowNum, toggleStreamingButton)

    return sendTab
