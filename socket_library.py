import socket

class client():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_client_connection(self, TCP_IP="192.168.1.97", TCP_PORT=8000):
        try:
            self.s.connect((TCP_IP, TCP_PORT))
        except socket.error:
            return 1

        return 0

    def send_string(self, message):
        b = bytes(message, "utf-8")
        try:
            self.s.send(message)
        except socket.error:
            print("Error: Failed to send message")
            return 1

        print("Message Sent!")
        return 0

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

