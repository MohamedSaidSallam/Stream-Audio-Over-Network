import socket
import pyaudio

PORT = 5000

p = pyaudio.PyAudio()
CHUNK = 1024

stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=48000,
                output=True,
                frames_per_buffer=CHUNK)

with socket.socket() as server_socket:
    print('started')
    server_socket.bind(('', PORT))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from " + address[0] + ":" + str(address[1]))

    data = conn.recv(CHUNK)
    while data != "":
        data = conn.recv(CHUNK)
        stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()
