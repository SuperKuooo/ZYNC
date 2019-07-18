import socket
import time

DEFAULT_IP = '192.168.1.118'
DEFAULT_PORT = 8000
BUFFER_SIZE = 4096


class Client:
    def __init__(self, conn: socket.socket = None):
        self.s = conn
        self.name = socket.gethostname()

    def set_client_connection(self, input_ip: str, input_port: int,
                              time_to_reconnect: int = 0, num_of_reconnects: int = 0) -> int:
        restart = num_of_reconnects
        if not num_of_reconnects:
            restart = float('inf')
        while restart > 0:
            restart -= 1
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.settimeout(2)
                self.s.connect((input_ip, input_port))
                break
            except socket.error:
                if time_to_reconnect:
                    print("Reconnecting in " + str(time_to_reconnect) + " seconds...")
                    time.sleep(time_to_reconnect)
                    continue
                return 1
        return 0

    def get_client_name(self):
        return self.name

    def confirm_connection(self, message=None):
        if not message:
            message = self.name + '///is online'
        self.s.settimeout(5)
        data = self.s.recv(BUFFER_SIZE).decode('utf-8')
        if data != message:
            print(message)
            print(data)
            raise UserWarning('Error: different echo value')
        return 0

    def recv(self, buffer_size: int):
        try:
            self.s.settimeout(2)
        except socket.error:
            return 1
        return self.s.recv(buffer_size)

    def send_string(self, message, raw: bool = False):
        b = message
        if not raw:
            b = bytes(message, 'utf-8')
        try:
            self.s.send(b)
        except socket.error:
            print('Error: Failed to send message')
            return 1
        return 0

    def send_image(self, location: str):
        try:
            with open(location, 'rb') as fp:
                b = bytearray(fp.read())
                self.s.sendall(b)
        except socket.error:
            print("Error: Failed to send image")
            return 1
        return 0

    def send_zip(self, location: str):
        try:
            with open(location, 'rb') as fp:
                self.s.sendall(fp.read())
                print("Sending")
        except socket.error:
            print("Error: Failed to send zip")
            return 1
        return 0

    def save_file(self, buffer, filepointer) -> int:
        # print('zip received')
        try:
            while True:
                data = self.s.recv(buffer)
                if not data:
                    break
                filepointer.write(data)
        except FileNotFoundError:
            # print('Error: Failed to save file')
            return 1
        return 0
        # print('zip saved')

    def close(self) -> int:
        # print(terminating)
        # self.send_string('terminating')
        self.s.close()
        return 0
