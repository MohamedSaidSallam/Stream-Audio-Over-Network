import tkinter as tk
from tkinter import ttk

from StreamAudioOverNetwork.firewall import toggleFirewall
from StreamAudioOverNetwork.network.networkutility import getLocalIP
from StreamAudioOverNetwork.streamaudio import ReceiveAudio
from StreamAudioOverNetwork.view.gridUtility import addRow

SEND_TAB_INDEX = 0


def getReceiveTab(notebook):
    receiveAudio = ReceiveAudio()
    receiveTab = ttk.Frame(notebook)

    rowNum = 0

    myIPLabel = tk.Label(receiveTab, text=f"My Local IP: {getLocalIP()}")
    rowNum = addRow(rowNum, myIPLabel)

    portLabel = tk.Label(receiveTab, text="Port: ")
    portTextBox = tk.Entry(receiveTab)
    portTextBox.insert(0, '5000')

    rowNum = addRow(rowNum, portLabel, portTextBox)

    def toggleReceiving():
        if receiveAudio.isStopped():
            receiveAudio.port = int(portTextBox.get())
            receiveAudio.start()

            toggleReceivingButton.configure(text="Stop Receiving")
            notebook.tab(SEND_TAB_INDEX, state="disabled")
        else:
            receiveAudio.stop()

            toggleReceivingButton.configure(text="Start Receiving")
            notebook.tab(SEND_TAB_INDEX, state="normal")

    toggleReceivingButton = tk.Button(receiveTab,
                                      text="Start Receiving",
                                      command=toggleReceiving
                                      )
    rowNum = addRow(rowNum, toggleReceivingButton)
    toggleFirewallgButton = tk.Button(receiveTab,
                                      text="Toggle Firewall",
                                      command=toggleFirewall
                                      )
    rowNum = addRow(rowNum, toggleFirewallgButton)

    return receiveTab
