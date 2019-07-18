import socket
import shutil
from typing import List
from .Client import *
import datetime

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
        temp = Client(_socket)
        if temp.send_string('0'):
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        elif temp.recv(1) == 1:
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        i += 1
    return _list


def time_stamp(_type: int = 0, dates=True, microsecond=True) -> str:
    if dates:
        stamp = rn()
    else:
        stamp = rn().time()

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


