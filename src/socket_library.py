import socket
import os
import shutil

BUFFER_SIZE = 4096

def zip_folder(output, target):
    print("Zipping Target...")
    shutil.make_archive(target, "zip", output)


class Client():
    def __init__(self, conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        self.s = conn
        self.name = socket.gethostname()


    def set_client_connection(self, TCP_IP="192.168.1.97", TCP_PORT=8000):
        try:
            self.s.connect((TCP_IP, TCP_PORT))
        except socket.error:
            print("Error: Failed to connect to server")
            return 1

        return 0

    def confirm_connection(self):
        self.s.settimeout(5)
        data = self.s.recv(BUFFER_SIZE)
        if data.decode("utf-8") != (self.name + "///is online"):
            raise "Error: Inequivalent echo"
        print("Echo Success")
        return 0

    def send_string(self, message):
        b = bytes(message, "utf-8")
        try:
            self.s.send(b)
        except socket.error:
            print("Error: Failed to send message")
            return 1
        print("Message sent")
        return 0

    def send_image(self, location):
        try:
            with open(location, 'rb') as fp:
                b = bytearray(fp.read())
                print(b[0])
                self.s.sendall(b)
        except socket.error:
            print("Error: Failed to send image")
            return 1
        print("Image sent")
        return 0

    def send_zip(self, location):
        with open(location, 'rb') as fp:
            self.s.sendall(fp.read())
            print("Sending")

    def close(self):
        self.s.close()


class Server:
    def __init__(self):
        self.list_of_connection = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def set_server_connection(self, TCP_IP="192.168.1.97", TCP_PORT=8000):
        try:
            self.s.bind((TCP_IP, TCP_PORT))
        except socket.error:
            print("Error: Failed to start server")
            return 1, 1
        return TCP_IP, TCP_PORT

    def echo_connection(self, conn, message):
        #print(message)
        message = message.decode("utf-8")
        try:
            temp = Client(conn)
            temp.send_string(message)
            self.list_of_connection.append(message.split('///')[0])
            temp.close()
        except socket.error:
            print("Error: Failed to echo client connection")

        return 0

    def close(self):
        return self.s.close()

    def listen(self, i):
        return self.s.listen(i)

    def accept(self):
        return self.s.accept()
