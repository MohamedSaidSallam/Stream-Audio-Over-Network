import tkinter as tk
from tkinter import ttk

from StreamAudioOverNetwork.firewall import toggleFirewall
from StreamAudioOverNetwork.network.networkutility import getLocalIP
from StreamAudioOverNetwork.streamaudio import ReceiveAudio
from StreamAudioOverNetwork.view.utility import setGrid


def getReceiveTab(notebook):
    receiveAudio = ReceiveAudio()
    receiveTab = ttk.Frame(notebook)

    myIPLabel = tk.Label(receiveTab, text=f"My Local IP: {getLocalIP()}")
    setGrid(myIPLabel, row=0)

    portLabel = tk.Label(receiveTab, text="Port: ")
    portTextBox = tk.Entry(receiveTab)
    portTextBox.insert(0, '5000')

    setGrid(portLabel, row=1, colSpan=1)
    setGrid(portTextBox, col=1, row=1, colSpan=1)

    def toggleReceiving():
        if receiveAudio.isStopped():
            receiveAudio.port = int(portTextBox.get())
            receiveAudio.start()
            toggleReceivingButton.configure(text="Stop Receiving")
        else:
            receiveAudio.stop()
            toggleReceivingButton.configure(text="Start Receiving")

    toggleReceivingButton = tk.Button(receiveTab,
                                      text="Start Receiving",
                                      command=toggleReceiving
                                      )
    setGrid(toggleReceivingButton, row=2)
    toggleFirewallgButton = tk.Button(receiveTab,
                                      text="Toggle Firewall",
                                      command=toggleFirewall
                                      )
    setGrid(toggleFirewallgButton, row=3)

    return receiveTab
