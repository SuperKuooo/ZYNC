# Tzu-Chi (Jerry), Kuo 2019
# jerrykuo820@gmail.com
# www.jerry-kuo.com
#
# Designed for Antiloop Studio. July 2019
# ========================================

import shutil
import datetime
import socket

from typing import List
from .client import Client

# TODO(Jerry): July 23, 2019
# Look into problem with relative import and stuff


def zip_folder(output: str, target: str) -> int:
    """ Zips the target directory and saves it to output directory

    :param output: Where the zipped directory is saved
    :param target: The target directory(Directory being zipped)
    :return: Return 1 if zip error. Else return 0
    """
    print('output: ', output)
    print('target: ', target)
    try:
        print('zipping target')
        # shutil.make_archive(output, "zip", target)
    except shutil.Error:
        print('Error: Zip failed')
        return 1
    return 0


def check_connection(list_of_connection: List[socket.socket]) -> List[socket.socket]:
    """ Checks if the passed in list of client connections are still alive

    :param list_of_connection: List of client connection
    :return: return the dead clients that were popped of the list
    """
    # TODO(Jerry): July 23, 2019
    # Think if communication needs to bi-directional
    # There is the multiple computers waiting glitch

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


def print_error(retval, message = None):
    if retval == Error.NoFile:
        print('Error: Failed to open file')
    elif retval == Error.NoTarget:
        print('Error: Empty Target')
    elif retval == Error.FailToSend:
        print('Error: Failed To send')
    elif retval == Error.FailToInitialize:
        print('Error: Failed To Initialize')
    elif retval == Error.FailSocketOp:
        print('Error: Socket operation failed')
    elif retval == Error.NoSuchOp:
        print('Error: Invalid input operation')
    elif retval == Error.CloseSocket:
        print('Error: Closing socket')
    elif message:
        print(message)


def time_stamp(
        _type: int = 0, dates: bool = True, microsecond: bool = True
) -> str:
    """ Creates time stamps

    :param _type: specifies the type of time stamp needed
    :param dates: If date is included in time stamp
    :param microsecond: if microsecond is included in time stamp
    :return: returns the created time stamp
    """
    if dates:
        stamp = datetime.datetime.now
    else:
        stamp = datetime.datetime.now().time()

    if _type == 1:
        temp = 'Conn: '
    elif _type == 2:
        temp = 'Error: '
    elif _type == 3:
        temp = 'project'
    else:
        temp = 'Debug: '

    if not microsecond:
        stamp = stamp.replace(microsecond=0)

    return str(stamp) + " " + temp


class Configuration:
    default_file = None

    def __init__(self):
        pass

    def set_config_file(self):
        try:
            f_pointer = open('./config.txt', 'r', encoding='utf-8')
        except FileNotFoundError:
            return 1

        for line in f_pointer:
            line = line.rstrip("\n").split(";")

            print(line)

        return 0


class Error(enumerate):
    EmptyResult = -1
    NoFile = 1
    NoRecvTarget = 2
    FailToSend = 3
    FailToInitialize = 4
    FailSocketOp = 5
    NoSuchOp = 6
    CloseSocket = 7

    Other = 99


if __name__ == '__main__':
    cf = Configuration()
    cf.set_config_file()
