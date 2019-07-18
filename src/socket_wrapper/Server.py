from .Utils import *
from typing import List, Union, Tuple

DATE = datetime.date.today()
rn = datetime.datetime.now
DEFAULT_IP = '192.168.1.118'
DEFAULT_PORT = 8000
BUFFER_SIZE = 4096


class Server:
    def __init__(self):
        self.list_of_connection = []
        self.list_of_observer = []
        self.name = socket.gethostname()
        self.s = None

    def set_server_connection(self, input_ip: str = DEFAULT_IP, input_port: int = DEFAULT_PORT,
                              attempt_to_reconnect: int = 0) -> Union[int, Tuple[str, int]]:
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((input_ip, input_port))
        except socket.error:
            print("Error: Failed to start server")
            if attempt_to_reconnect:
                print("Retrying in " + str(attempt_to_reconnect) + " seconds...")
                time.sleep(attempt_to_reconnect)
                self.set_server_connection(
                    input_ip, input_port, attempt_to_reconnect)
            return 1
        return input_ip, input_port

    def set_list_of_connection(self, _socket=None, operation: int = 0, index: int = None) -> int:
        if operation == 0:
            # Append
            self.list_of_connection.append(_socket)
        elif operation == 1:
            # Set new list
            self.list_of_connection = _socket
        elif operation == 2:
            # Delete item by index
            if index is not None:
                self.list_of_connection.pop(index)
        elif operation == 3:
            # Clears the connection
            self.list_of_connection.clear()
        else:
            # print('Error: Invalid operation')
            return 1
        return 0

    def set_list_of_observer(self, _observer=None, operation=0, index=None) -> int:
        if operation == 0:
            self.list_of_observer.append(_observer)
        elif operation == 1:
            self.list_of_observer = _observer
        elif operation == 2:
            if not index:
                self.list_of_observer[index].close()
                self.list_of_observer.pop(index)
        elif operation == 3:
            for obs in self.list_of_observer:
                obs.close()
            self.list_of_observer.clear()
        else:
            print('Error: Invalid operation')
            return 1
        return 0

    def get_num_of_connection(self) -> int:
        return len(self.list_of_connection)

    def get_num_of_observer(self) -> int:
        return len(self.list_of_observer)

    def get_list_of_connection(self, index: int = None) -> Union[List[socket.socket], socket.socket]:
        if not index:
            return self.list_of_connection
        else:
            return self.list_of_connection[index]

    def get_list_of_observer(self, index: int = None):
        if index is None:
            return self.list_of_observer
        return self.list_of_observer[index]

    def get_server_name(self) -> str:
        return self.name

    def echo_connection(self, conn: socket.socket, message):
        message = message.decode("utf-8")
        try:
            temp = Client(conn)
            temp.send_string(message)
            self.set_list_of_connection(conn)
        except socket.error:
            print("Error: Failed to echo client connection")
        return 0

    def broadcast_string(self, message, client_index: int = None):
        if client_index is None:
            target_audience = self.get_list_of_connection()
        else:
            target_audience = self.get_list_of_connection(client_index)

        for conn in target_audience:
            try:
                temp = Client(conn)
                temp.send_string(message)
                # print('Sending zip')
            except socket.error:
                print("Error: Failed to send message")
                return 1
        return 0

    def broadcast_zip(self, location: str, client_index: int = None):
        if client_index is None:
            target_audience = self.get_list_of_connection()
        else:
            target_audience = self.get_list_of_connection(client_index)

        for conn in target_audience:
            try:
                with open(location, 'rb') as fp:
                    conn.sendall(fp.read())
            except socket.error:
                print("Error: Failed to send zip")
                return 1
        return 0

    def close(self):
        for conn in self.list_of_connection:
            conn.close()
        for obs in self.list_of_observer:
            obs.close()
        return self.s.close()

    def listen(self, size: int):
        return self.s.listen(size)

    def accept(self):
        return self.s.accept()
