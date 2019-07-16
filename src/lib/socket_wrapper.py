import socket
import os
import time
import shutil
from typing import List, Union, Tuple
import datetime
from watchdog.observers import Observer as OBS

DATE = datetime.date.today()
rn = datetime.datetime.now
DEFAULT_IP = '192.168.1.118'
DEFAULT_PORT = 8000
BUFFER_SIZE = 4096


def zip_folder(output: str, target: str) -> int:
    # print("Zipping Target...")
    try:
        shutil.make_archive(output, "zip", target)
    except shutil.Error:
        return 1
        # print("Error: Failed to zip file")
    return 0


def check_connection(list_of_connection: List[socket.socket]) -> List[socket.socket]:
    _list = []
    i = 0

    for _socket in list_of_connection:
       # print(rn(), _socket)
        temp = Client(_socket)
       #  print(temp.get_client_name())

        if temp.send_string('0'):
            # print(rn(), 'send')
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        elif temp.recv(1) == 1:
            # print(rn(), 'recv')
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        i += 1
    return _list


def time_stamp(_type: int = 0, dates=True, microsecond=True) -> str:
    if dates:
        stamp = rn()
    else:
        stamp = rn().time()
    temp = None

    if _type == 1:
        temp = "Conn: "
    elif _type == 2:
        temp = 'Error: '
    elif _type == 3:
        temp = 'project'
    else:
        temp = 'Debug: '

    if not microsecond:
        stamp = stamp.replace(microsecond=0)

    return str(stamp) + " " + temp


class Client:
    def __init__(self, conn: socket.socket = None):
        self.s = conn
        self.name = socket.gethostname()

    def set_client_connection(self, TCP_IP: str, TCP_PORT: int, time_to_reconnect:int=0, num_of_reconnects:int=0) -> int:
        restart = num_of_reconnects
        if not num_of_reconnects:
            restart = float('inf')
        while restart > 0:
            restart -= 1
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.settimeout(2)
                self.s.connect((TCP_IP, TCP_PORT))
                break
            except socket.error:
                # print(TCP_IP, TCP_PORT)
                if time_to_reconnect:
                    print("Reconnecting in " + str(time_to_reconnect) + " seconds...")
                    time.sleep(time_to_reconnect)
                    continue
                    # print("Starting client...")
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
        # print('Echo Success')
        return 0

    def recv(self, buffer_size: int):
        try:
            self.s.settimeout(2)
            return self.s.recv(buffer_size)
        except socket.error:
            # print('Warning: Timeout')
            return 1

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


class Server:
    def __init__(self):
        self.list_of_connection = []
        self.list_of_observer = []
        self.name = socket.gethostname()
        self.s = None
    
    def set_server_connection(self, TCP_IP:str=DEFAULT_IP, TCP_PORT:int=DEFAULT_PORT, attempt_to_reconnect:int=0) -> Union[int, Tuple[str, int]]:
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((TCP_IP, TCP_PORT))
        except socket.error:
            print("Error: Failed to start server")
            if attempt_to_reconnect:
                print("Retrying in " + str(attempt_to_reconnect) + " seconds...")
                time.sleep(attempt_to_reconnect)
                self.set_server_connection(
                    TCP_IP, TCP_PORT, attempt_to_reconnect)
            return 1
        return (TCP_IP, TCP_PORT)

    def set_list_of_connection(self, _socket:Client=None, operation:int=0, index:int=None) -> int:
        if operation == 0:
            # Append
            self.list_of_connection.append(_socket)
        elif operation == 1:
            # Set new list
            self.list_of_connection = _socket
        elif operation == 2:
            # Delete item by index
            if index != None:
                self.list_of_connection.pop(index)
        elif operation == 3:
            # Clears the connection
            self.list_of_connection.clear()
        else:
            # print('Error: Invalid operation')
            return 1
        return 0

    def set_list_of_observer(self, _observer:'Observer'=None, operation=0, index=None) -> int:
        if operation == 0:
            self.list_of_observer.append(_observer)
        elif operation == 1:
            self.list_of_observer = _observer
        elif operation == 2:
            if index != None:
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

    def get_list_of_connection(self, index:int=None) -> Union[List[socket.socket], socket.socket]:
        if not index:
            return self.list_of_connection
        else:
            return self.list_of_connection[index]

    def get_list_of_observer(self, index:int=None) -> Union[List['Observer'], 'Observer']:
        if index == None:
            return self.list_of_observer
        return self.list_of_observer[index]

    def get_server_name(self) -> str:
        return self.name

    def echo_connection(self, conn:socket.socket, message):
        message = message.decode("utf-8")
        try:
            temp = Client(conn)
            temp.send_string(message)
            self.set_list_of_connection(conn)
        except socket.error:
            print("Error: Failed to echo client connection")
        return 0

    def broadcast_string(self, message, client_index:int=None):
        if client_index == None:
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

    def broadcast_zip(self, location:str, client_index:int=None):
        if client_index == None:
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

    def listen(self, size:int):
        return self.s.listen(size)

    def accept(self):
        return self.s.accept()


class Observer:
    def __init__(self, server=Server, lib_path=str, target_path=str):
        self.obs = OBS()
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.handler = Handler(server, lib_path, target_path)
        # TODO: add a timing mode
        # self.mode = True

    def set_server(self, server=Server):
        self.server = server
        return 0

    def get_target_path(self) -> str:
        return self.target_path

    def start_observe(self, recursive:bool=False) -> int:
        try:
            self.obs.schedule(self.handler, self.tot_path, recursive)
            self.obs.start()
        except RuntimeError:
            return 1
        return 0

    def close(self) -> int:
        try:
            self.obs.stop()
            self.obs.join()
        except RuntimeError:
            return 1
        return 0


class Handler:
    def __init__(self, server:Server, lib_path:str, target_path:str):
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.last_success = 'tdoay'
        self.last_attempt = '56 mins ago'
        self.total_attempts = 16
        self.save_directory = '/usr'

    def dispatch(self, event):
        if(event.src_path.endswith('.log')):
            print('Logfile Modified')
            filename = os.path.join('./archive', self.target_path, str(DATE))
            if zip_folder(filename, self.tot_path):
                print('Error: ZIP failed')
            else:
                print('zipped')
            
            self.server.broadcast_string('zip')
            time.sleep(0.5)
            print('sending zip')
            self.server.broadcast_zip(os.path.join(
                './archive', self.target_path, str(DATE) + '.zip'))
            print('done shipping')
        else:
            return 1
        return 0

    def get_details(self):
        return [self.last_success, self.last_attempt, self.total_attempts, self.save_directory]
