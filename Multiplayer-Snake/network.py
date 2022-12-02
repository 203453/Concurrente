import socket
import pickle

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 5555
        self.server = IPAddr

        self.addr = (self.server, self.port)
        self.connect()

    def get(self):
        return self.client.recv(8192)

    def connect(self):
        self.client.connect(self.addr)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(8192))
        except socket.error as e:
            print(e)
