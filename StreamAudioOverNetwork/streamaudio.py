import socket
import pyaudio
import threading

CHUNK = 1024


class ReceiveAudio():
    port = None

    def __init__(self):
        self._stop_event = threading.Event()
        self._stop_event.set()

    def logic(self):
        self._p = pyaudio.PyAudio()
        self._stream = self._p.open(format=pyaudio.paInt16,
                                    channels=2,
                                    rate=48000,
                                    output=True,
                                    frames_per_buffer=CHUNK)
        with socket.socket() as server_socket:
            server_socket.bind(('', self.port))
            server_socket.listen(1)
            conn, _ = server_socket.accept()

            data = conn.recv(CHUNK)
            while data != "":
                if self.isStopped():
                    self._stop_event.clear()
                    break
                data = conn.recv(CHUNK)
                self._stream.write(data)

        self._stream.stop_stream()
        self._stream.close()
        self._p.terminate()

    def start(self):
        if not self.isStopped():
            raise Exception()
        self._stop_event.clear()
        self._thread = threading.Thread(target=self.logic)
        self._thread.start()

    def stop(self):
        if self.isStopped():
            raise Exception()
        self._stop_event.set()

    def isStopped(self):
        return self._stop_event.is_set()


class SendAudio():
    def __init__(self, port, deviceIndex, host=socket.gethostname()):
        self._stop_event = threading.Event()
        self._host = host
        self._p = pyaudio.PyAudio()
        device = self._p.get_device_info_by_index(deviceIndex)
        self._stream = self._p.open(format=pyaudio.paInt16,
                                    channels=device["maxOutputChannels"],
                                    rate=int(device["defaultSampleRate"]),
                                    input=True,
                                    frames_per_buffer=CHUNK,
                                    input_device_index=device['index'],
                                    as_loopback=True)
        self.port = port

    def logic(self):
        with socket.socket() as client_socket:
            client_socket.connect((self._host, self.port))
            while True:
                if self.isStopped():
                    self._stop_event.clear()
                    break
                data = self._stream.read(CHUNK)
                client_socket.send(data)

        self._stream.stop_stream()
        self._stream.close()
        self._p.terminate()

    def start(self):
        if self.isStopped():
            raise Exception()
        self._stop_event.clear()
        self._thread = threading.Thread(target=self.logic)
        self._thread.start()

    def stop(self):
        if not self.isStopped():
            raise Exception()
        self._stop_event.set()

    def isStopped(self):
        return self._stop_event.is_set()
