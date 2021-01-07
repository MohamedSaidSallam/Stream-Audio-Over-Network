import socket
import pyaudio

HOST = socket.gethostname()
PORT = 5000

CHUNK = 1024
p = pyaudio.PyAudio()

device = p.get_device_info_by_index(8)

channelcount = device["maxInputChannels"] if (
    device["maxOutputChannels"] < device["maxInputChannels"]) else device["maxOutputChannels"]
stream = p.open(format=pyaudio.paInt16,
                channels=channelcount,
                rate=int(device["defaultSampleRate"]),
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=device['index'],
                as_loopback=True)


print("Recording")

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        data = stream.read(CHUNK)
        client_socket.send(data)
