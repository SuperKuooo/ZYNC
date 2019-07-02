import socket
import os


class client():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_client_connection(self, TCP_IP="192.168.1.97", TCP_PORT=8000):
        try:
            self.s.connect((TCP_IP, TCP_PORT))
        except socket.error:
            print("Error: Failed to connect to server")
            return 1

        return 0

    def send_string(self, message):
        b = bytes(message, "utf-8")
        try:
            self.s.send(b)
        except socket.error:
            print("Error: Failed to send message")
            return 1
        print("Message Sent!")
        return 0

    def send_image(self, location=os.getcwd()):
        with open(location, 'rb') as fp:
            b = bytearray(fp.read())
            print(b[0])
            self.s.sendall(b)
        return 0

    def send_zip(self, location, zipped):
        if(not zipped):
            print("Zipping")
        else:
            print("Sending")

    def close(self):
        self.s.close()


class server():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_server_connection(self, TCP_IP="192.168.1.97", TCP_PORT=8000):
        try:
            self.s.bind((TCP_IP, TCP_PORT))
        except socket.error:
            return 1
        return 0

    def close(self):
        self.s.close()

    def listen(self, i):
        self.s.listen(i)

    def accept(self):
        return self.s.accept()
